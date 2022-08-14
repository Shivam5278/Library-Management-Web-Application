from app import app, db
from flask import render_template, url_for, flash, session, request, get_flashed_messages, redirect, request
import datetime

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

@app.route('/delete/<book_n>', methods=['GET', 'POST'])
def delete(book_n):
    form = forms.DeleteTaskForm()
    bookn = models.Books.query.get(book_n)
    if bookn:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(bookn)
                db.session.commit()
                flash('Book deleted successfully!')
            return redirect(url_for('home'))
        return render_template('delete.html', form=form, book_n=book_n, title=bookn)
    flash(f'Please select a book before deleting.')
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
        flash('Book added successfully!')
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
@app.route('/members/<b>', methods = ['POST', 'GET'])
def members(b=None):
    members1 = models.Members.query.all()
    todo  = request.args.get('todo', None)
    if todo == 'delete':
        member2 = models.Members.query.get(b)
        if member2:
            db.session.delete(member2)
            db.session.commit()
            flash('Member details deleted successfully!')
            return redirect(url_for('members'))
        flash('Please select a member to delete details.')
        return redirect(url_for('members'))
    else:
        if request.method =="POST":
            print('x')
        else:
            if b==None:
                return render_template('members.html', members1=members1, id=99999)
            else:
                return render_template('members.html', members1=members1, id= b)



@app.route('/addme', methods = ['POST', 'GET'])
def addme():
    form = forms.AddMemberForm()
    if form.validate_on_submit():
        found_member=models.Members.query.filter_by(memid_m=form.mem_id.data).first()
        if found_member:
            flash('Member with this ID already present!')
        else:
            task = models.Members(name_m=form.name.data, memid_m=form.mem_id.data)
            db.session.add(task)
            db.session.commit()
            flash('Member added successfully.')
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






@app.route('/isreturn<val>',methods = ['POST', 'GET'])
def isreturn(val):
    form = forms.AddTransactionForm()
    date= datetime.date.today()
    memberid  = request.args.get('memberid', None)
    bookid  = request.args.get('bookid', None)
    members = models.Members.query.all()
    books = models.Books.query.all()

    found_member=models.Members.query.filter_by(id_m=memberid).first()
    found_book=models.Books.query.filter_by(id=bookid).first()



    if val == "issue":
        if request.method=='POST':
            if form.validate_on_submit():

                task = models.Transactions(name_t=form.name.data, memid_t=form.mem_id.data, title_t=form.book.data, issue_t=date, due_t=form.rdate.data, rent_t=form.rent.data, type_t=val)
                db.session.add(task)
                db.session.commit()
                return redirect(url_for('home'))
            else:
                flash(f'{form.errors}')
                return redirect(url_for('addme'))
        return render_template('isreturn.html', transaction=val, member=found_member, book=found_book, form=form, date= date, members=members)
    elif val == "return":
        return render_template('isreturn.html', transaction=val, member=found_member, book=found_book, form=form, date= date, members=members, books=books)
    else:
        flash('Page not found!')
        return redirect(url_for('home'))
