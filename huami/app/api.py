#Importieren der notwendigen Module und Klassen
from app import app, db
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User, recipe 
from flask import jsonify, abort, url_for, request

#Initialisieren der Authentifizierun
auth = HTTPBasicAuth()
tauth = HTTPTokenAuth()

@app.route('/api/nutzer/<int:id>', methods=['GET'])
@tauth.login_required
def get_user(id):
    data = User.query.get_or_404(id).to_dict()
    return jsonify(data)

#Route um einen bestimmten Nutzer abzurufen
@app.route('/api/nutzer', methods=['GET'])
@tauth.login_required
def get_users():
#Abfragen des Nutzers mit der angegebenen ID und Konvertieren in ein Dictionary
    data = User.to_collection()
    return jsonify(data)

#Funktion zur Überprüfung eines Tokens
@tauth.verify_token
def verify_token(atoken):
    return User.check_token(atoken) if atoken else None

#Route um einen API-Token zu erhalten
@app.route('/api/apitoken', methods=['POST'])
@auth.login_required
def get_token():
#Generieren und Zurückgeben eines API Tokens für angemeldete Benutzer
    atoken = auth.current_user().get_token()
    db.session.commit()
    return jsonify({'Token': atoken})

#Route um die Rezepte eines bestimmten Nutzers abzurufen
@app.route('/api/nutzer/<int:id>/recipes', methods=['GET'])
@tauth.login_required
def get_recipe(id):
    user = User.query.get_or_404(id)
    recipe = user.rec_to_collection()
    return jsonify(recipe)

#Funktion zur Überprüfung des Benutzernamens und des Passworts
@auth.verify_password
def verify_password(user, password):
    user = User.query.filter_by(username=user).first()
    if user and user.check_password(password):
       return user
