from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SECRET_KEY"] = "13f9d18375c494a4561aff0a0fd2d66d"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    img = db.Column(db.String(60),nullable=False,default="./static/images/placeholder.png")
    password = db.Column(db.String(60),unique=False,nullable=False)
    post = db.relationship("Post",backref="author",lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.img}')"

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),unique=False,nullable=False)
    post_date = db.Column(db.Date,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.post_date}')"


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