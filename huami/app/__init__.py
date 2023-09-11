#Importieren der Flask-Bibliothek und anderer notwendiger Module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap
import os

#Initialisieren der Flask-Anwendung
app = Flask(__name__)
#Konfiguration der Flask Anwendung aus einer Konfigurationsklasse
app.config.from_object(Config)
#Initialisieren der SQLAlchemy Datenbank Erweiterung
db = SQLAlchemy(app)
#Initialisieren der Flask Migrate Erweiterung für Datenbankmigrationen
migrate = Migrate(app, db)
#Initialisieren des LoginManagers für Benutzer-Authentifizierung
login = LoginManager(app)
login.login_view = 'login'
#Initialisieren der Flask Bootstrap Erweiterung für das Frontend-Styling
bootstrap = Bootstrap(app)

#Importieren von Routen, Modellen und API-Endpunkten
from app import routes, models, api
