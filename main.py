from flask import Flask, render_template, request
import json
import importlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    db = json.loads(open("/Users/jstenger/Documents/workspace/remote_machine2/database/programs2.json").read())
    print(db)
    return render_template('home.html', jsondb=json.dumps(db), db = db)


@app.route('/run', methods=['GET', 'POST'])
def run():
    # return str(request.form.get("programs"))

    return str(runFile("Scripts", str(request.form.get("program")), [9])), 200
   
    
def runFile(location, name, args):
    # for x in range len()
    file = importlib.import_module(location + "." + name)
    # print(file)
    return file.main(*args)


if __name__ == "__main__":
    app.run()