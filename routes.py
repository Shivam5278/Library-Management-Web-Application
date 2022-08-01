from app import app, db
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from datetime import datetime

import sys
import models
import forms
#from datas import data
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    books = models.Books.query.all()
    return render_template('home.html', books=books)
