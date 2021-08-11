from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

 

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    eye_color = db.Column(db.String(250), unique=True, nullable=False)
    gender = db.Column(db.String(100), unique=True, nullable=False)
    species = db.Column(db.String(100), unique=True, nullable=False)
    vehicle = db.Column(db.String(250), unique=True, nullable=False)
    film = db.Column(db.String(250), unique=True, nullable=False)

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    diameter = db.Column(db.Integer, unique=True, nullable=False)
    population = db.Column(db.Integer, unique=True, nullable=False)
    climate = db.Column(db.String(250), unique=True, nullable=False)
    film = db.Column(db.String(250), unique=True, nullable=False)

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    crew = db.Column(db.String(250), unique=True, nullable=False)
    film = db.Column(db.String(250), unique=True, nullable=False)
    
class Species(db.Model):
    __tablename__ = 'species'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False) 
    film = db.Column(db.String(250), unique=True, nullable=False)

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    character = db.Column(db.String(250), unique=True, nullable=False)


