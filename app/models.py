from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # name field
    email = db.Column(db.String(100), unique=True, nullable=False)  # email field
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    
    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"