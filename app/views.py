from flask import render_template, redirect, request, url_for
from app import app
from .App import App

application = App()


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
                return redirect(url_for('homepage'))
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
                return redirect(url_for('homepage'))
        error = 'Invalid Username/Password'
    return render_template('Sign_in.html', form=form, error=error)

# @app.route('/lists', methods=['GET', 'POST'])
# def lists():
#     return render_template("Lists.html")
#
#
# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     # logout_user()
#     return redirect(url_for('Sign_in.html'))
