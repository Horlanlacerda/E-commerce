from flask import render_template, session, request, url_for, flash,redirect
from loja import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from.models import User
import os

@app.route('/admin')
def admin():
    if'email' not in session:
        flash('Fazer login no sistema primeiro.', category='danger')
        return redirect(url_for('login'))
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
    if request.method == 'POST' and form.validate():
        user = User.query.filter(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            session['email'] = form.email.data
            flash(f'Obrigado {form.email.data} por logar!', category='success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Não foi possível fazer login!', category='danger')
    return render_template('admin/login.html', form=form, title='Página de Login')
