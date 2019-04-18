from flask import Flask, render_template, request
import json, importlib, unittest, os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    db = json.loads(open("/Users/jstenger/Documents/workspace/remote_machine/database/programs.json").read())
    print(db)
    return render_template('home.html', db=map(json.dumps, db))


@app.route('/run', methods=['GET', 'POST'])
def run():
    # return str(request.form.get("programs"))
    return str(runFile("Scripts", str(request.form.get("program")), [9]))
   
    
<<<<<<< Updated upstream
def runFile(location, name, args):
    # for x in range len()
    file = importlib.import_module(location + "." + name)
    # print(file)
    return file.main(*args)

=======
def runFile(name,*args):
    index = os.path.join(os.path.dirname(__file__),'database/programs.json')
    with open(index, 'r') as raw_file:
        scriptStorage = json.loads(raw_file.read())
        #print(scriptStorage[name])
    try:
        location = scriptStorage[name]["path"]
        #print(location)
    except KeyError:
        return "Unexpected Error: The script is either missing or has an invalid location"
    try:
        file = importlib.import_module(location+"."+name) 
        output = file.main(*args)
    except Exception as excpt:
        output = "Unexpected Error: "+str(excpt)
    return output  
>>>>>>> Stashed changes

class testRunFile(unittest.TestCase):
    def testFibCorrect(self):
        self.assertEqual(runFile('Fibonacci',2),1)
        self.assertEqual(runFile('Fibonacci',23),28657)
    def testFibErrors(self):
        self.assertEqual(runFile('Fibonacci',2,3),'Unexpected Error: main() takes 1 positional argument but 2 were given')
        self.assertEqual(runFile('FakeProgram',2),'Unexpected Error: The script is either missing or has an invalid location')
if __name__ == "__main__":
<<<<<<< Updated upstream
    app.run()
=======
    unittest.main()
    app.run()
>>>>>>> Stashed changes
