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
{% endblock %} <--It will automatically find the end block(main)-->
```

