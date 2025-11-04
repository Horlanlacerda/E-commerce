from flask import render_template, session, request, url_for, flash,redirect
from loja import db, app
from .models import Marca, Categoria
from .forms import Addprodutos

@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marca(name='getmarca')
        db.session.add(marca)
        flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addmarca'))
    return render_template('/produtos/addmarca.html', marcas='marcas')


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == "POST":
        getmarca = request.form.get('categoria')
        cat = Categoria(name='getmarca')
        db.session.add(cat)
        flash(f'A categoria {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('/produtos/addmarca.html')


@app.route('/addproduto', methods=['GET', 'POST'])
def addproduto():
    form = Addprodutos(request.form)
    return render_template('produtos/addproduto.html', title='Cadastrar Produtos', form=form)