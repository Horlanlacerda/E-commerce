from flask import render_template, session, request, url_for, flash,redirect
from loja import db, app

@app.route('addmarca', methods=['GET', 'POST'])
def addmarca():
    return render_template('/produtos/addmarca.html')
