from flask import Flask # from the flask module import the Flask class

# OOP -> Object Oriented Paradigm
app = Flask(__name__) # create an instance of Flask (an object)

@app.get("/") # Flask decorator
def index(): # View function 
    me = { # Python dictionary
        "first_name": "Tyler",
        "last_name": "Salvato",
        "hobbies": "Music",
        "is_active": True
    }
    return me # return statement (JSON) 

# A decorator is simply a function that wraps another function
# This means that the wrapping function takes a function as a parameter
# high level example:
# def wrapper_function(other_func):
    #do stuff here
    # value = other_func()
    #do stuff here
    # return value

