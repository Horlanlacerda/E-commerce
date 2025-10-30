from flask import render_template, session, request, url_for
from loja import app, db

@app.route('/')

def home():
    return "Seja bem vindo so sistema em flask!"