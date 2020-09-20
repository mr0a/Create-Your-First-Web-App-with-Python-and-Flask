from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a instance of flask app
#You can call it with anyname
app = Flask(__name__) # Pass the name to the flask initializer
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


db = SQLAlchemy(app)

from routes import *
# This is equivalent to copying all codes here

if  __name__ == '__main__':
    app.run(debug=True)