from blog import app
from blog import db
from blog.models import User

with app.app_context():
   db.create_all()
   u1 = User(name = "Damilola",email_address = "ezekielakinfenwa@gmail.com",password_hash = "12345678")
   db.session.add(u1)
   db.session.commit()