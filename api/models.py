from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    is_sale_opportunity = db.Column(db.Boolean, default=True)
    cars = db.relationship('Car', backref='owner', lazy=True)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)
