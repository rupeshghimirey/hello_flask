from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def print_dojo():
    return "Dojo!"

@app.route('/say/<nameInput>')
def greet_name(nameInput):
    return "Hi " + nameInput +"!";

@app.route('/repeat/<int:num>/<string:name>')
def repeat_names(num,name):
    return f"{num*name}"



if __name__=="__main__":
    app.run(debug=True) 
