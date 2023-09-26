from blog import app,db
from flask import render_template,redirect,url_for,flash
from blog.forms import SignupForm,LoginForm,BlogForm
from blog.models import User,Blog
from flask_login import login_user,logout_user,current_user,login_required
from blog.utils import create_placeholder,generate_date,generate_time


@app.route('/')
def home():
    blogs = Blog.query.all()
    user = User()
    return render_template("index.html",blogs = blogs,user = user)

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():

        user_to_create = User(name = form.username.data,email_address = form.email_address.data,
                              password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash(message = "You have succesfully created your account",category="success")
        return redirect(url_for("home"))

    if form.errors != {}:
        err_msg = form.errors.values()
        for err in err_msg:
            flash(message=err, category="danger")
    return render_template('signup.html',form = form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_to_check = User.query.filter_by(name = form.username.data).first()
        if user_to_check:
            if user_to_check.check_password(form.password.data):
                login_user(user_to_check)
                flash(message = "You have Logged in succesfully as {0}".format(form.username.data), category = "success")
                return redirect(url_for("home"))
            else:
                flash(message = "{0} passsword is wrong".format(form.username.data), category = "warning")
        else:
            flash(message = "{0} does not exist".format("User"), category = "warning")

    return render_template('login.html', form = form)
@app.route('/logout')
def logout():
    logout_user()
    flash(message="You have been logged out succesfully", category = "info")
    return redirect(url_for("home"))

@app.route('/createblog',methods=['GET', 'POST'])
@login_required
def createblog():
    form = BlogForm()
    if form.validate_on_submit():
        blog_to_add = Blog(topic = form.topic.data,
                           placeholder = create_placeholder(form.content.data),
                           content = form.content.data,
                           date = generate_date(),
                           time = generate_time(),
                           owner = current_user.id)
        db.session.add(blog_to_add)
        db.session.commit()
        flash(message = "Blog has been created succesfully",category="success")
        return redirect(url_for("home"))
    return render_template('createblog.html',form = form)

@app.route('/blogs')
def allblogs():
    blogs = Blog.query.all()
    user = User()
    return render_template('allblogs.html', blogs = blogs, user = user)
@app.route('/viewblog/<int:id>')
def viewblog(id):
    blog = Blog.query.get_or_404(id)
    user = User()
    return render_template('viewblog.html',blog = blog,user = user)
        

    