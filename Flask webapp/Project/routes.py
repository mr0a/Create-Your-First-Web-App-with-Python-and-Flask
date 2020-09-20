from app import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import db,Task
from datetime import datetime

import forms

@app.route('/')
@app.route('/index') 
# We can also use same function for multiple routes.
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        #print(Task.query.all())
        flash('Task Added')
        return redirect(url_for('index'))
    return render_template('add.html', form = form)

@app.route('/edit/<int:task_id>', methods=['GET','POST'])#<int:var_name> is a way to pass info to our function
def edit(task_id):
    task = Task.query.get(task_id)
    #print(task)
    form = forms.AddTaskForm()
    
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("Task Updated")
            return redirect(url_for('index'))

        form.title.data = task.title
        return render_template('edit.html',form=form, task_id=task_id)
    flash("Task not found")
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods = ['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteForm()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("Task deleted")
            return redirect(url_for('index'))
        return render_template('delete.html',form= form, task_id = task.id, title = task.title)
    flash("Task doesnot exist")
    return redirect(url_for('index'))