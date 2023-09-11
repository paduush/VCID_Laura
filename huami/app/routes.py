#Importieren von Flask-Modulen und anderen notwendigen Abhänigkeiten
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EmptyForm, addrecipe
from app.models import User, recipe

#Routen und die dazugehörigen Funktionen

#Startseite
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Huami - Home')

#Einloggen
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user, remember=form.remember_me.data)
        return redirect('index')
    return render_template('login.html', title='Sign In', form=form)

#Ausloggen
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#Registrieren
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#Rezeptseite für den eingeloggten Benutzer
@app.route('/recipies/<username>', methods=['GET', 'POST'])
@login_required
def recipes(username):
    recipe = current_user.own_recipe()
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('recipes.html',recipe=recipe)

#Hinzufügen eines neuen Rezepts
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    entry = addrecipe()
    if entry.validate_on_submit():
        addrcp = recipe(name=entry.Name.data, subtext=entry.Subtext.data,time=entry.Time.data, saison=entry.Saison.data, ingred1=entry.Ing1.data,ingred2=entry.Ing2.data,ingred3=entry.Ing3.data,ingred4=entry.Ing4.data,ingred5=entry.Ing5.data,ingred6=entry.Ing6.data,ingred7=entry.Ing7.data,ingred8=entry.Ing8.data,ingred10=entry.Ing10.data,ingred11=entry.Ing11.data,ingred12=entry.Ing12.data,ingred13=entry.Ing13.data,ingred14=entry.Ing14.data,ingred15=entry.Ing15.data,ingred16=entry.Ing16.data,ingred17=entry.Ing17.data,ingred18=entry.Ing18.data,ingred19=entry.Ing19.data, steps1=entry.Stp1.data, steps2=entry.Stp2.data,steps3=entry.Stp3.data,steps4=entry.Stp4.data,steps5=entry.Stp5.data,steps6=entry.Stp6.data,steps7=entry.Stp7.data,steps8=entry.Stp8.data,steps10=entry.Stp10.data,steps11=entry.Stp11.data,steps12=entry.Stp12.data,steps13=entry.Stp13.data,steps14=entry.Stp14.data,steps15=entry.Stp15.data,steps16=entry.Stp16.data,steps17=entry.Stp17.data,steps18=entry.Stp18.data,steps19=entry.Stp19.data,making=entry.Make.data, rec=current_user)
        db.session.add(addrcp)
        db.session.commit()
        flash('Das Rezept wurde gespeichert')
        return redirect(url_for('add'))
    return render_template('add.html', entry=entry)
