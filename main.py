from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
import json
import importlib
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/jstenger/Documents/workspace/remote_machine/Scripts'
ALLOWED_EXTENSIONS = set(['py'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            dbfile = open(os.path.join("database/programs.json"), 'r+')
            file.save(os.path.join(app.instance_path, app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
            description = ""
            if request.form['description'] is not None:
                description = request.form['description']
            db = json.loads(dbfile.read())
            db.append({'description': description, 'name': file.filename.split('.')[0]})
            dbfile.seek(0)
            json.dump(db, dbfile)
            dbfile.truncate()

            # return redirect(url_for('uploaded_file', filename=file.filename))
    db = json.loads(open(os.path.join("database/programs.json")).read())
    return render_template('upload.html' , db=db)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def main():
    db = json.loads(open(os.path.join("database/programs.json")).read())
    return render_template('home.html', jsondb=json.dumps(db), db=db)


@app.route('/run', methods=['GET', 'POST'])
def run():
    return str(runFile("Scripts", str(request.form.get("program")), [int(request.form.get("input"))])), 200


def runFile(location, name, args):
    print(args)
    # for x in range len()
    file = importlib.import_module(location + "." + name)
    # print(file)
    return file.main(*args)


if __name__ == "__main__":
    app.run()