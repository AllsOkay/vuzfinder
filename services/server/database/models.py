from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    role = db.Column(db.String(255), nullable=False, server_default='User')

class Uni(db.Model):
    __tablename__ = 'unis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    full_name = db.Column(db.Text)
    adress = db.Column(db.Text)
    description = db.Column(db.Text)
    picture_name = db.Column(db.Text)
    region = db.Column(db.Text)
    eg_score = db.Column(db.Text)
    eg_score_contract = db.Column(db.Text)
    eg_score_budget = db.Column(db.Text)
    areas = db.Column(db.Text)
    price = db.Column(db.Text)
    place_contract = db.Column(db.Text)
    place_budget = db.Column(db.Text)
    cost = db.Column(db.Text)

class Quiz(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answers = db.Column(db.Text)