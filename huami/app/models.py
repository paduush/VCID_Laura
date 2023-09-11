#Importieren der notwendigen Module
from app import login
from app import db, login
from time import time
from flask import url_for
from flask_login import UserMixin
from datetime import datetime, timedelta
import base64
import os
from werkzeug.security import generate_password_hash, check_password_hash

#Definition des UserModells anhand SQLAlchemy
class User(UserMixin, db.Model):
    #Definieren der Tabellenspalten
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(256), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    rec = db.relationship('recipe', backref='rec', lazy='dynamic')
    atoken = db.Column(db.String(32), index=True, unique=True)
    runout = db.Column(db.DateTime)

    #Methode zur Darstellung des Benutzers
    def __repr__(self):
        return '<User {}>'.format(self.username)

    #Methode zur Festlegung des Passworts
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    #Methode zur Überprüfung des Passworts
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    #Methode zur Abfrage der eigenen Rezepte eines Benutzers
    def own_recipe(self):
        own = recipe.query.filter_by(user_id=self.id)
        return own.order_by(recipe.timestamp.desc())

    #Methode zur Erstellung eines JSON-Datenformats für den Benutzer
    def to_dict(self):
        data = {
            'id': self.id,
            'Nutzername': self.username,
            'Mailadresse': self.email
        }
        return data

    #Methode zur Überprüfung eines Tokens
    @staticmethod
    def check_token(atoken):
        nutzer = User.query.filter_by(atoken=atoken).first()
        if nutzer is None or nutzer.runout < datetime.utcnow():
            return None
        return nutzer

    #Methode zur Erstellung einer Sammlung aller Benutzer
    @staticmethod
    def to_collection():
        user = User.query.all()
        data = {'items': [item.to_dict() for item in user]}
        return(data)


    def rec_to_collection(self):
        data = {'items': [item.to_dict() for item in self.rec]}
        return data

    #Methode zur Erstellung und Aktualisierung eines Tokens für den Benutzer
    def get_token(self, expires_in=72000):
        now = datetime.utcnow()
        if self.atoken and self.runout > now + timedelta(seconds=60):
            return self.token
        self.atoken = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.runout = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.atoken

    #Methode zur Ungültigmachung eines Tokens
    def revoke_token(self):
       self.outrun = datetime.utcnow() -timedelta(seconds=1)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


#Definition des Rezept Modells mit SQLAlchemy
class recipe(db.Model):
#Definieren der Tabellenspalten
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    subtext = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.Integer, index=True, nullable=False)
    saison = db.Column(db.String(256), nullable=False)
    making = db.Column(db.String(256), nullable=False)
    ingred1 = db.Column(db.String(256), index=True)
    ingred2 = db.Column(db.String(256), index=True)
    ingred3 = db.Column(db.String(256), index=True)
    ingred4 = db.Column(db.String(256), index=True)
    ingred5 = db.Column(db.String(256), index=True)
    ingred6 = db.Column(db.String(256), index=True)
    ingred7 = db.Column(db.String(256), index=True)
    ingred8 = db.Column(db.String(256), index=True)
    ingred10 = db.Column(db.String(256), index=True)
    ingred11 = db.Column(db.String(256), index=True)
    ingred12 = db.Column(db.String(256), index=True)
    ingred13 = db.Column(db.String(256), index=True)
    ingred14 = db.Column(db.String(256), index=True)
    ingred15 = db.Column(db.String(256), index=True)
    ingred16 = db.Column(db.String(256), index=True)
    ingred17 = db.Column(db.String(256), index=True)
    ingred18 = db.Column(db.String(256), index=True)
    ingred19 = db.Column(db.String(256), index=True)
    steps1 = db.Column(db.String(256), index=True)
    steps2 = db.Column(db.String(256), index=True)
    steps3 = db.Column(db.String(256), index=True)
    steps4 = db.Column(db.String(256), index=True)
    steps5 = db.Column(db.String(256), index=True)
    steps6 = db.Column(db.String(256), index=True)
    steps7 = db.Column(db.String(256), index=True)
    steps8 = db.Column(db.String(256), index=True)
    steps10 = db.Column(db.String(256), index=True)
    steps11 = db.Column(db.String(256), index=True)
    steps12 = db.Column(db.String(256), index=True)
    steps13 = db.Column(db.String(256), index=True)
    steps14 = db.Column(db.String(256), index=True)
    steps15 = db.Column(db.String(256), index=True)
    steps16 = db.Column(db.String(256), index=True)
    steps17 = db.Column(db.String(256), index=True)
    steps18 = db.Column(db.String(256), index=True)
    steps19 = db.Column(db.String(256), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    #Methode zur Darstellung des Rezepts
    def __repr__(self):
        return f'<Recipe {self.id}>'.format(self.body)
    #Dies wurde aufgund von Unachtsamkeit in das Datenbank Schema eingepflegt.

    #Methode zur Erstellung eines JSON-Datenformats für das Rezept
    def to_dict(self):
        data = {
            '00_id' : self.id,
            '01_Name des Rezepts': self.name,
            '02_Untertitel': self.subtext,
            '03_Erfassungsdatum': self.timestamp,
            '04_Zubereitungsdauer': self.time,
            '05_Saison': self.saison,
            '06_Zubereitungsart': self.making,
            '07_Zutaten': {
                 'Zutat 01': self.ingred1,
                 'Zutat 02': self.ingred2,
                 'Zutat 03': self.ingred3,
                 'Zutat 04': self.ingred4,
                 'Zutat 05': self.ingred5,
                 'Zutat 06': self.ingred6,
                 'Zutat 07': self.ingred7,
                 'Zutat 08': self.ingred8,
                 'Zutat 09': self.ingred10,
                 'Zutat 10': self.ingred11,
                 'Zutat 11': self.ingred12,
                 'Zutat 12': self.ingred13,
                 'Zutat 13': self.ingred14,
                 'Zutat 14': self.ingred15,
                 'Zutat 15': self.ingred16,
                 'Zutat 16': self.ingred17,
                 'Zutat 17': self.ingred18,
                 'Zutat 18': self.ingred19
},
            '08_Schritte': {

                 'Schritt 01': self.steps1,
                 'Schritt 02': self.steps2,
                 'Schritt 03': self.steps3,
                 'Schritt 04': self.steps4,
                 'Schritt 05': self.steps5,
                 'Schritt 06': self.steps6,
                 'Schritt 07': self.steps7,
                 'Schritt 08': self.steps8,
                 'Schritt 09': self.steps10,
                 'Schritt 10': self.steps11,
                 'Schritt 11': self.steps12,
                 'Schritt 12': self.steps13,
                 'Schritt 13': self.steps14,
                 'Schritt 14': self.steps15,
                 'Schritt 15': self.steps16,
                 'Schritt 16': self.steps17,
                 'Schritt 17': self.steps18,
                 'Schritt 18': self.steps19
}}
        return data

    @staticmethod
    def to_collection():
        resources = qrcode.query.all()
        data = {'items': [item.to_dict() for item in resources]}
        return(data)
