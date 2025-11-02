from flask import render_template, session, request, url_for, flash,redirect
from loja import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from.models import User
import os

@app.route('/')
def home():
    return render_template('admin/index.html', title='Página Admininistrativa')



@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit() # sobe os dados para o bd
        flash(f'Obrigado {form.name.data} por registrar', category='success')
        return redirect(url_for('home'))
    return render_template('admin/registrar.html', form=form, title="Página de Registros")



@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm(request.form)
    return render_template('admin/login.html', form=form, title='Página de Lógin')
