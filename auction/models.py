from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False )
    password_hash = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment', backref='user')

class Watch(db.Model):
    __tablename__ = 'watches'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    comments = db.relationship('Comment', backref='watch')
    bids = db.relationship('Bid', backref='watch')

    
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name) 

class Itemcreate(db.Model):
    __tablename__ = 'Items'
    id = db.relationship('id', backref='Items')
    make = db.Column(db.String(10))
    model = db.Column(db.String(10))
    movement = db.Column(db.String(10))
    starting_bid = db.Column(db.String(10))
    image = db.Column(db.String(400))
    description = db.Column(db.String(400))
    year = db.Column(db.String(10))
    condition = db.Column(db.String(10))

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer,
    db.ForeignKey('watches.id'))
     
    def __repr__(self):
        return "<Comment: {}>".format(self.text)


class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer,
    db.ForeignKey('watches.id'))


    def __repr__(self):
        return "<Bid: {}>".format(self.text)
