from flask import render_template, redirect, request, url_for, session
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
        username = request.form['username']
        password = request.form['password']
        if application.validate_on_signup(username, password):
            if request.form['confirmpassword'] == password:
                session[username] = username
                return redirect(url_for('index', username=username))
            error1 = 'Passwords do not match'
        error2 = 'User already exists'
    return render_template('Sign_up.html', form=form, error1=error1, error2=error2)


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    form = request.form
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if application.validate_on_signin(username, password):
            session[username] = username
            return redirect(url_for('index', username=username))
        error = 'Invalid Username/Password'
    return render_template('Sign_in.html', form=form, error=error)


@app.route('/index/<username>', methods=['POST', 'GET'])
def index(username):
    return render_template('index.html', username=username)


# @app.route('/addbucketlist', methods=['POST', 'GET'])
# def addbucketlist():
#     form = request.form
#     if request.method == 'POST':
#         title = request.form['title']
#         bucketlist.add_bucketlist(title)
#         return redirect(url_for('additem', form=form, title=title))
#     return render_template('Add-bucketlist.html', form=form)


@app.route('/additems', methods=['GET', 'POST'])
def additems():
    form = request.form
    error = None
    if request.method == 'POST':
        title = request.form['title']
        item = request.form['item']
        if title:
            bucketlist.additems(title, item)
            return redirect(url_for('additems', form=form, title=title))
        error = 'Add title first'
    return render_template('Add-item.html', form=form, error=error)


@app.route('/edittitle/<title>', methods=['GET', 'POST'])
def edit_title(title):
    form = request.form
    if request.method == 'POST':
        new_title = form['new_title']
        bucketlist.edittitle(title, new_title)
        return redirect(url_for('additems'))
    return redirect(url_for('additems'))


# @app.route('/edititem/<item>', methods=['GET', 'POST'])
# def edit_item(item):
#     form = request.form
#     if request.method == 'POST':
#         new_item = form['new_item']
#         bucketlist.edit_items(item, new_item)
#         return redirect(url_for('additem'))


@app.route('/deletelist/<title>', methods=['POST'])
def deletelist(title):
    if request.form == 'POST':
        bucketlist.deletelist(title)
        return redirect(url_for('additems'))


@app.route('/deleteitem', methods=['POST'])
def deleteitem():
    pass


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    # logout_user()
    return redirect(url_for('signin'))
