# Create-Your-First-Web-App-with-Python-and-Flask

## Video 1: Introduction
This is the introduction to the app we are going to make and the rhyme platform
- In this project we will be building a todo app where we will be able to add, edit or delete tasks using flask, python and SQLalchemy.

## Video 2: A Minimal App
We wil create a basic app which does nothing but just to keep our files in structure.  
The starter files are in the templates/starter folder.
* We will create a file app.py which is the entry point to our app
* Do you know about `__name__` in python?
    * If you run the file directly python will assign the special variable `__name__ = __main__`  
* Import Flask  
`from flask import Flask`
* Create a instance of Flask with variable name app (you can name it anything)  
`app = Flask(__name__)`
* Call run() method in app if we execute the file directly  
```python3
if __name__ == '__main__':
    app.run(debug=True)
```
* debug is optional and set to true:
    *  View error in our webpage if occurs.
    * The server automatically reloads when any change is made to the files. :smile: 
* Run the app using `python3 app.py` in terminal.  
    * This will start a web server listening on port 5000. If you open the port using your favourite browser you will get 404 Page Not Found as we havent set the web server to do anything when someone access any webpage.
* We need to use route to show content when someone access.  
```python3
@app.route('/') 
# This is a decorator to tell our server that we need to run index function at '/'.
def index():
    return "Hello World"
```
This is a simple route which returns "Hello World" (you can return any html too) when root page is accessed.  
Now our server knows that it has to fun the function when "/" route is accessed.

## Video 3: Templates
* In `return "Hello World"` instead of html or text you can return a html templates(jinja2 templating engine) using render_template function in flask.
    ```python3
    from flask import render_template
    ...
    def index():
        return render_template('index.html')
    ...

    ```
    * Place the html files inside a directory named `templates`.
* Another cool thing in **jinja2** (a templating engine) is that you can pass information and use it in your templates.
    >app.py  
    ```python3
    def index():
        return render_template('index.html',current_title = "Custom")
    ```
    * Now the variable current_title is accessible in the html by **{{ current_title }}**
    > index.html  
    ```
    <!DOCTYPE html>
        <html>
    <head>
        <title>{{current_title}}</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
    </html>
    ```
* This is pretty powerful because we can create dynamic web pages using these templates very easily.
* Now you can create a basic web server which serves dynamic webpages at any route address.

## Video 4: Extending HTML Templates

Let's assume there are two pages in our site `index.html` and `about.html`.  
There maybe common code in both the pages except some difference in the page content.  
We can extend templates to prevent rewriting of code.  
> base.html
 ```html
    <h1>Title of the Website</h1>
    <h3>Subheader: something</h3>
    <hr>
    <p> <a href='/'>Index Page</a> &nbsp; <a href="/about">About Page</a></p>

    {% block main%}

    {% endblock main%}
```
* `{% block main %}` will let us to add different content at different pages or different parts of a same page with similar other blocks.
> index.html
```html
{% extends "base.html" %}
```
* This will add the content of `base.html` in the index page.
> about.html
```html
{% extends "base.html"%}

{% block main %}
<p>This is about page</p>
{% endblock %} <--It will automatically find the endblock(main)-->
```
* Now we have learnt jinja templating, so we can create templates easily.

## Video 5: Refactoring and Forms
If we have a large website with many routes putting all code in a same file is not easy to manage.  
So code refactoring makes it easy to manage code.
* Now we will move the routes information into another file `routes.py` and import it into our `app.py`.
>app.py
```python3
from flask import Flask

# Create a instance of flask app
#You can call it with anyname
app = Flask(__name__) # Pass the name to the flask initializer

#import routes after instanciating flask app
from routes import *
# This is equivalent to copying all codes here

if  __name__ == '__main__':
    app.run(debug=True)
```
>routes.py
```python3
from app import app
from flask import render_template

@app.route('/')
@app.route('/index') 
# We can also use same function for multiple routes.
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
```
* Now we have reformatted our code lets proceed with forms.  
Lets create a new file `forms.py` and we will use this to import in our main code.  
>forms.py
```python3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
```
* StringField - is equivalent to the text field we use in HTML forms
* SubmitField - I guess you know it
* When we use wtforms we make classes which extend from class `Flaskform`  
> forms.py
```python3
class AddTaskForm(FlaskForm):
    title = Stringfield('Title', validators = [DataRequires()])
# To use validator import - from wtforms.validators import DataRequired
    submit = SubmitField('Submit')
```
* Now we have created the form class let's import it and create a form in about page
> forms.py
```python3
import forms
...
def about():
    form = forms.AddTaskForm()
    return render_template('about.html', form = form)
```
* Now the form is accessible in the `about.html` template
But before setting up the form, Flask forms implement a security feature `csrf_token()` to prevent cross-site-forgery-request.  
Also the `csrf_token()` function needs a *secret key* to generate tokens.

* In `app.py` add `app.config['SECRET_KEY'] = 'some-secret'` after instanciating flask app.
* Now lets add the form in `about.html`  
> about.html
```html
<form method="post">
    {{ form.csrf_token() }} <!--To generate csrf token-->
    {{ form.title }}
    {{ form.submit }}
</form>
```
* Now a secure form will be added in the about page of our website.
* If you submit any data using the form it will show Method not allowed error.

## Video 6: Handling POST Requests
By default flask expects for `GET` requests. We can modify to allow `POST` requests.  
* To do that we need to pass argument method to route as follows:  
`@app.route('/about', method = ['GET', 'POST'])`  
Now the about page accepts `POST` requests and the values are accessible to us.
* Add the following code to the function def of about about page (the form accepting page):
```python3
if form.validate_on_submit():
    print("Submitted value is ", form.title.data)
    return render_template('about.html', form = form, data = form.title.data)
```
* Now we will be able to see the POST data submitted from the terminal as well as it is also available in `about.html` template in data variable.
> about.html
```html
...
{% if data %}
    <h1>{{ data }}</h1>
{% endif %} <!--In jinja templates all the block must have end block-->
```