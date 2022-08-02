from app import app, db
from flask import render_template, url_for, flash, session, request, get_flashed_messages, redirect, request
from datetime import datetime

import sys
import models
import forms
from datas import bookid
@app.route('/')
@app.route('/index')
@app.route('/home', methods = ['POST', 'GET'])
def home():
    books = models.Books.query.all()
    if request.method =="POST":

        session["book_name"] = request.form["bknm"]
        return redirect(url_for("booke"))
    else:
        return render_template('home.html', books=books)

@app.route("/book")
def booke():
    if "book_name" in session:
        book = session["book_name"]
        return f"<h1>{book}</h1>"
    else:
        return redirect(url_for("home"))

@app.route('/delete/<book_n>', methods=['GET', 'POST'])
def delete(book_n):
    form = forms.DeleteTaskForm()
    bookn = models.Books.query.get(book_n)
    if bookn:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(bookn)
                db.session.commit()
                flash('book deleted')
            return redirect(url_for('home'))
        return render_template('delete.html', form=form, book_n=book_n, title=bookn)
    flash(f'Task with id {book_n} does not exit')
    return redirect(url_for('home'))

@app.route('/add/<a>', methods=['GET', 'POST'])
def add(a):
    form = a
    found_book = models.Books.query.filter_by(title=form).first()
    if found_book:
        flash('Book already in list')
    else:
        task = models.Books(title=form, author="a" ,quantity=10)
        db.session.add(task)
        db.session.commit()
        flash('Book added')
        return redirect(url_for('home'))
    return redirect(url_for('adds'))

@app.route('/adds', methods=['GET', 'POST'])
def adds():
    #
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        found_book = models.Books.query.filter_by(title=form.title.data).first()
        if found_book:
            flash('Book already in list')
        else:
            x=form.title.data
            booksa=bookid(x)
            s=[]
            #print(titlex)
            #task = models.Books(title=booksa[1], author="a" ,quantity=6)
            #db.session.add(task)
            #db.session.commit()
            #flash('Book added')
            return render_template('adds.html',s=booksa, form=form)
        #return redirect(url_for('home'))
    return render_template('adds.html', form=form)
