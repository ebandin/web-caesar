from flask import Flask, request

app = Flask(__name__) 
app.config['DEBUG']= True

form = """
<!doctype html> 
<html> 
    <head> 
    <style> 
        form{
            background-color: #eee; 
            padding: 20px; 
            margin: 0 auto; 
            width: 540px; 
            font: 16px sans-serif; 
            border-radius: 10px; 
        }
        textarea {
            margin: 10px 0; 
            width: 540px; 
            height: 120px; 
        }
    </style> 
    </head> 
    <body> 

        <form action = "/hello" method = "post"> 
            <label for="rot"> Rotate by:</label> 
            <input id="rot" type="text" name="rot"/ value="0"> 
            <input id="Code-word" type="textarea" name="code_word"/> 
            <input type="submit"/> 

        </form> 
    </body> 
</html> 
"""

@app.route("/")
def index(): 
    return form 
#initialize the html 
@app.route("/hello", methods = ['POST'])
def hello(): 
    code_word = request.form['code_word']
    pass
app.run()
