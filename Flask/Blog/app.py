from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "13f9d18375c494a4561aff0a0fd2d66d"

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


if __name__ == "__main__":
    app.run(debug=True,port=8080)