from blog import db
from blog import login_manager
from flask_login import UserMixin
from blog import bcrypt

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    topic = db.Column(db.String(),nullable = False)
    placeholder = db.Column(db.String(length = 30),nullable = False)
    content = db.Column(db.String(),nullable = False)
    date = db.Column(db.String(),nullable = False)
    time = db.Column(db.String(),nullable = False)
    owner = db.Column(db.Integer(),db.ForeignKey("user.id"))

    def __repr__ (self):
        return "{0}".format(self.topic)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(),nullable = False, unique = True)
    email_address = db.Column(db.String(),nullable = False, unique = True)
    password_hash = db.Column(db.String(),nullable = False,unique = True)
    blogs = db.relationship("Blog",backref = "owned_user",lazy = True)

    def __repr__ (self):
        return "{0}".format(self.name)
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self,pain_text_password):
        self.password_hash = bcrypt.generate_password_hash(pain_text_password).decode("UTF-8")
    
    def check_password(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)
    


