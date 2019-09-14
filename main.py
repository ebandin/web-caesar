from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__) 
app.config['DEBUG']= True

form = """
<!doctype html> 
<html> 
    <head> 
    <style> 
        form {{
            background-color: #eee; 
            padding: 20px; 
            margin: 0 auto; 
            width: 540px; 
            font: 16px sans-serif; 
            border-radius: 10px;
        }}
        textarea {{
            margin: 10px 0; 
            width: 540px; 
            height: 120px; 
        }}
    </style> 
    </head> 
    <body> 

        <form action = "/hello" method = "post"> 
            <label for="rot"> Rotate by:</label> 
            <input id="rot" type="text" name="rot" value="0"/> 
            <h1> <textarea id="Code-word" type="textarea" name="code_word"> {0}</textarea></h1> 
            <input type="submit"/> 

        </form> 
    </body> 
</html> 
"""

@app.route("/")
def index(): 
    return form.format("Enter your word to be coded")
#initialize the html 

@app.route("/hello", methods= ['POST'])
def encrypt(): 
    rot = int(request.form['rot'])
    code_word = str(request.form['code_word'])
    finals = rotate_string(code_word, rot)
    
    return form.format(finals)


app.run()
