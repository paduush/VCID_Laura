#Importieren der notwenigen Module und Klassen
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User, recipe

#Login Formular
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

#Registrierungs Formular
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

#Benutzername-Validierung
#Überprüft, ob der Benutzername bereits existiert
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
#E-Mail-Validierung
#Überprüft, ob die E-Mail-Adresse bereits verwendet wird
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

#Leeres Formular
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

#Rezept hinzufügen Formular
class addrecipe(FlaskForm):
    #Felder für die Rezeptinformationen
    Name = StringField('Name des Gerichts', validators=[DataRequired(), Length(min=1, max=256)])
    Subtext = StringField('Geben Sie ihrem Rezept einen Catchy Subtext', validators=[DataRequired(), Length(max=256)])
    Time = StringField('Wie lange dauert ihr Rezept (in Minuten)', validators=[DataRequired(), Length(max=256)])
    Saison = StringField('Wann eignet sich ihr Rezept am besten (Sommer, Winter, Immer)', validators=[DataRequired(), Length(max=256)])
    Make = StringField('Kocht oder Backt man das Rezept', validators=[DataRequired(), Length(max=256)])
    #Felder für Zutaten
    Ing1 = StringField('Zutaten - (Max 256 Zeichen)', validators=[DataRequired(), Length(max=256)])
    Ing2 = StringField(validators=[Length(max=256)])
    Ing3 = StringField(validators=[Length(max=256)])
    Ing4 = StringField(validators=[Length(max=256)])
    Ing5 = StringField(validators=[Length(max=256)])
    Ing6 = StringField(validators=[Length(max=256)])
    Ing7 = StringField(validators=[Length(max=256)])
    Ing8 = StringField(validators=[Length(max=256)])
    Ing10 = StringField(validators=[Length(max=256)])
    Ing11 = StringField(validators=[Length(max=256)])
    Ing12 = StringField(validators=[Length(max=256)])
    Ing13 = StringField( validators=[ Length(max=256)])
    Ing14 = StringField(validators=[Length(max=256)])
    Ing15 = StringField(validators=[ Length(max=256)])
    Ing16 = StringField(validators=[Length(max=256)])
    Ing17 = StringField(validators=[Length(max=256)])
    Ing17 = StringField(validators=[Length(max=256)])
    Ing18 = StringField(validators=[Length(max=256)])
    Ing19 = StringField(validators=[Length(max=256)])
    #Felder für Zubereitungsschirtte
    Stp1 = StringField('Wie wird ihr Rezept zubereitet? - (Max 256 Zeichen)', validators=[DataRequired(), Length(max=256)])
    Stp2 = StringField(validators=[Length(max=256)])
    Stp3 = StringField(validators=[Length(max=256)])
    Stp4 = StringField(validators=[Length(max=256)])
    Stp5 = StringField(validators=[Length(max=256)])
    Stp6 = StringField(validators=[Length(max=256)])
    Stp7 = StringField(validators=[Length(max=256)])
    Stp8 = StringField(validators=[Length(max=256)])
    Stp10 = StringField(validators=[Length(max=256)])
    Stp11 = StringField(validators=[Length(max=256)])
    Stp12 = StringField(validators=[Length(max=256)])
    Stp13 = StringField(validators=[Length(max=256)])
    Stp14 = StringField(validators=[Length(max=256)])
    Stp15 = StringField(validators=[Length(max=256)])
    Stp16 = StringField(validators=[Length(max=256)])
    Stp17 = StringField(validators=[Length(max=256)])
    Stp18 = StringField(validators=[Length(max=256)])
    Stp19 = StringField(validators=[Length(max=256)])
    #Rezept publizieren
    submit = SubmitField('Submit')



