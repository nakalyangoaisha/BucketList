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


@app.route('/addtitle', methods=['POST', 'GET'])
def addtitle():
    form = request.form
    if request.method == 'POST':
        title = request.form['title']
        if bucketlist.addtitle(title):
            return redirect(url_for('additems', form=form, title=title))
        error = 'Bucketlist with title already exists'
        return redirect(url_for('addtitle', form=form, error=error))


@app.route('/additems', methods=['GET'])
def additems():
    return render_template('Add-items.html')


@app.route('/saveitem/<title>', methods=['POST', 'GET'])
def saveitem(title):
    form = request.form
    item = request.form['item']
    if request.method == 'POST':
        if bucketlist.saveitem(title, item) and item is not None:
            redirect(url_for('additems', title=title))
        error = 'Item already in list'
        return redirect(url_for('saveitem', form=form, error=error))


@app.route('/edit_title/<title>', methods=['GET', 'POST'])
def edit_title(title):
    form = request.form
    if request.method == 'POST':
        new_title = form['new_title']
        bucketlist.edittitle(title, new_title)
        return redirect(url_for('additems'))
    return redirect(url_for('additems', new_title=title))


@app.route('/edititem/<item>', methods=['GET', 'POST'])
def edit_item(item):
    form = request.form
    if request.method == 'POST':
        new_item = form['new_item']
        bucketlist.edit_items(item, new_item)
        return redirect(url_for('additem'))


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
