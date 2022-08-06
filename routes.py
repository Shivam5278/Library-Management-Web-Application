from app import app, db
from flask import render_template, url_for, flash, session, request, get_flashed_messages, redirect, request
from datetime import datetime

import sys
import models
import forms
from datas import bookid
@app.route('/')
@app.route('/index')
@app.route('/home/<a>', methods = ['POST', 'GET'])
def home(a=None):
    books = models.Books.query.all()
    if request.method =="POST":
        print(x)
    else:
        if a==None:
            return render_template('home.html', books=books, id=99999)
        else:
            return render_template('home.html', books=books, id= a)

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

@app.route('/add/<b>', methods=['GET', 'POST'])
def add(b):
    a  = request.args.get('a', None)
    p  = request.args.get('p', None)
    found_book = models.Books.query.filter_by(title=b).first()
    if found_book:
        flash('Book already in Library!')
    else:
        task = models.Books(title=b, author=a ,publisher=p, quantity=10)
        db.session.add(task)
        db.session.commit()
        flash('Book added')
        return redirect(url_for('home'))
    return redirect(url_for('adds'))

@app.route('/adds', methods=['GET', 'POST'])
def adds():
    entry = forms.AddTaskForm()
    if entry.validate_on_submit():
        found_book = models.Books.query.filter_by(title=entry.title.data).first()
        if found_book:
            flash('Book already available in Library!')
        else:
            x=entry.title.data
            book_s, author_s, publisher_s=bookid(x)
            return render_template('adds.html',books=book_s, authors=author_s, publishers= publisher_s, form=entry, ret=True)
        #return redirect(url_for('home'))
    return render_template('adds.html', form=entry, ret=False)


@app.route('/members', methods = ['POST', 'GET'])
def members():
    members1 = models.Members.query.all()
    if request.method =="POST":
        print('x')
        #session["book_name"] = request.form["bknm"]
        #return redirect(url_for("booke"))
    else:
        return render_template('members.html', members1=members1)


@app.route('/addme', methods = ['POST', 'GET'])
def addme():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        task = models.Members(name_m=form.title.data, memid_m=5)
        db.session.add(task)
        db.session.commit()
        flash('Member added')
        return redirect(url_for('members'))
    return render_template('addme.html', form=form)



@app.route('/transactions', methods = ['POST', 'GET'])
def transactions():
    transactions1 = models.Transactions.query.all()
    if request.method =="POST":
        print('x')
        #session["book_name"] = request.form["bknm"]
        #return redirect(url_for("booke"))
    else:
        return render_template('transactions.html', transactions1=transactions1)






@app.route('/isreturn<val>')#, method = ['POST', 'GET'])
def isreturn(val):
    if val == "issue":
        return render_template('isreturn.html', transaction=val)
    elif val == "return":
        return render_template('isreturn.html', transaction=val)
    else:
        flash('Page not found!')
        return redirect(url_for('home'))
