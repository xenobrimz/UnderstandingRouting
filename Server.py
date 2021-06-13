from flask import Flask  
app = Flask(__name__)   

@app.route('/')     
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')     
def dojo():
    return 'Dojo!' 

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say_hello(name):
    return "Hello " + name

@app.route('/repeat/<num>/<_str>') 
def repeat(num, _str):
    new_str =""
    for i in range(int(num)):
        new_str += " " + str(_str)
    return new_str
    

if __name__=="__main__":   
    app.run(debug=True)    