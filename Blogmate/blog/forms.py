from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from blog.models import User


class SignupForm(FlaskForm):

    def validate_username(self,username_to_validate):
        user =  User.query.filter_by(name = username_to_validate.data).first()
        if user:
            raise ValidationError("Username already exists, please try another username")
        
    def validate_email_address(self,email_address_to_validate):
        user =  User.query.filter_by(email_address = email_address_to_validate.data).first()
        if user:
            raise ValidationError("Email already exists, please try another email")
    
    username = StringField(label = "Username", validators=[DataRequired(),Length(min = 6)])
    email_address = StringField(label = "Email Address", validators=[DataRequired(),Length(min = 6),Email()])
    password1 = PasswordField(label = "Enter Password",validators=[DataRequired(),Length(min = 8)])
    password2 = PasswordField(label = "Confirm Password",validators=[DataRequired(),Length(min = 8),EqualTo("password1")])
    submit = SubmitField(label = "Submit")

class LoginForm(FlaskForm):
    username = StringField(label = "Username", validators=[DataRequired(),Length(min = 6)])
    password = PasswordField(label = "Enter Password",validators=[DataRequired(),Length(min = 8)])
    submit = SubmitField(label = "Submit")

class BlogForm(FlaskForm):
    topic = StringField(label = "Blog Title",validators=[DataRequired(),Length(min = 6)])
    content = TextAreaField(label = "Blog Contents",validators=[DataRequired(),Length(min = 50)])
    submit = SubmitField(label = "Submit")