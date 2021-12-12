from flask import render_template,url_for,flash,redirect
from app.forms import RegistrationForm, LoginForm
from app import app
from app.models import User, Post

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html",title="home")

@app.route("/classifier")
def classifier():
    return render_template("classifier.html",title="classifier")

@app.route("/tags")
def tags():
    return render_template("tags.html",title="tags")

@app.route("/archives")
def archives():
    return render_template("archives.html",title="archives")

@app.route("/about")
def about():
    return render_template("about.html",title="about")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
