from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import MetaData

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Integer, nullable=False)
    registered_date = db.Column(db.DateTime, default=datetime.utcnow)

    notes = db.relationship('Notes', backref="author", lazy=True)
    categories = db.relationship('Categories', backref="category_author", lazy=True)

    def __repr__(self):
        return f"{self.username}"

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categories_name = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Categories('{ self.categories_name }')"

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable=True)	
    date_saved = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Notes('{self.id}', '{self.date_saved}', '{self.categories}'), '{self.user_id}')"




