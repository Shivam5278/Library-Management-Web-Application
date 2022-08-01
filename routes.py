from app import app, db
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from datetime import datetime

import sys
import models
import forms
#from datas import data
@app.route('/')
@app.route('/index')
def index():
    tasks = "a"
    #print(data)
    return render_template('index.html', tasks=tasks)


@app.route('/search', methods=['GET', 'POST'])
def search():
    search = 'akmaks'#forms.AddTaskForm()
    #if search.validate_on_submit():

    #    flash('These are the books for your search')
    #    return redirect(url_for('index'))
    return render_template('search.html', search=search), search

x=search
sys.modules[__name__] = search
