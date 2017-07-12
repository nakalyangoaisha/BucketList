from flask import render_template, redirect, request, url_for
from app import app
from .App import App
from .models import BucketList

application = App()
bucketlist = BucketList()


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = request.form
    error1 = None
    error2 = None
    if request.method == 'POST':
        data1 = request.form['username']
        data2 = request.form['password']
        if application.validate_on_signup(data1, data2):
            if request.form['confirmpassword'] == data2:
                return redirect(url_for('index', data1=data1))
            error2 = 'Passwords do not match'
        error1 = 'User already exists'
    return render_template('Sign_up.html', form=form, error1=error1, error2=error2)


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    form = request.form
    error = None
    if request.method == 'POST':
        data1 = request.form['username']
        data2 = request.form['password']
        if application.validate_on_signin(data1, data2):
            return redirect(url_for('index', data1=data1))
        error = 'Invalid Username/Password'
    return render_template('Sign_in.html', form=form, error=error)


@app.route('/index/<data1>', methods=['POST', 'GET'])
def index(data1):
    return render_template('index.html', data1=data1)


@app.route('/addbucketlist', methods=['POST', 'GET'])
def addbucketlist():
    form = request.form
    if request.method == 'POST':
        data = request.form['title']
        bucketlist.add_bucketlist(data)
        return redirect(url_for('additem', form=form, title=data))
    return render_template('Add-bucketlist.html', form=form)


@app.route('/additems/<title>', methods=['GET', 'POST'])
def additem(title):
    form = request.form
    if request.method == 'POST':
        item = request.form['item']
        bucketlist.add_items(title, item)
        return redirect(url_for('additem', form=form, title=title))
    return render_template('Add-bucketlist.html', form=form)


@app.route('/edittitle/<title>', methods=['GET', 'POST'])
def edit_title(title):
    form = request.form
    if request.method == 'POST':
        new_title = form['new_title']
        bucketlist.edit_title(title, new_title)
        return redirect(url_for('additem'))
    return redirect(url_for('additem'))


# @app.route('/edititem/<item>', methods=['GET', 'POST'])
# def edit_item(item):
#     form = request.form
#     if request.method == 'POST':
#         new_item = form['new_item']
#         bucketlist.edit_items(item, new_item)
#         return redirect(url_for('additem'))



@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    # logout_user()
    return redirect(url_for('Sign_in.html'))
