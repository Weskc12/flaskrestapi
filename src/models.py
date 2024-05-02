from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tableName__="user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    __tableName__="planets"
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    Favorite = db.relationship("Favorites", backref="planets")
    
    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "climate": self.climate,
            "terrain": self.terrain,
            "diameter": self.diameter,
            
        }

class Vehicles(db.Model):
    __tableName__="vehicles"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(120), unique=True, nullable=False)
    vehicle_class = db.Column(db.String(80), unique=False, nullable=False)
    cost_in_credits = db.Column(db.String(80), unique=False, nullable=False)
    Favorite = db.relationship("Favorites", backref="vehicles")
    
    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "cost_in_credits": self.cost_in_credits,
            
        }

class People(db.Model):
    __tableName__= "people"
    id = db.Column(db.Integer, primary_key=True)
    persons_name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.String(80), unique=False, nullable=False)
    Favorite = db.relationship("Favorites", backref="people")
    
    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "persons_name": self.persons_name,
            "height": self.height,
            "mass": self.mass,            
            
        }    
    
class Favorites(db.Model):
    __tableName__= "favorties"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,ForeignKey('user.id'),nullable=True)
    person_id= db.Column(db.Integer,ForeignKey('people.id'),nullable=True)
    planet_id = db.Column(db.Integer,ForeignKey('planets.id'),nullable=True)
    vehicle_id = db.Column(db.Integer, ForeignKey('vehicles.id'),nullable=True)
    
    

    def serialize(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id,           
            
        }