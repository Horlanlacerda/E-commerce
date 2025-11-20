from email.mime import image
from sqlalchemy.exc import IntegrityError
from flask import render_template, session, request, url_for, flash,redirect, session, current_app
from loja import db, app, photos
from .models import Marca, Categoria, Addproduto
from .forms import Addprodutos
import secrets, os


@app.route('/')
def home():
    produtos = Addproduto.query.filter(Addproduto.stock > 0)
    marcas = Marca.query.join(Addproduto, (Marca.id == Addproduto.marca_id)).all()
    categorias = Categoria.query.join(Addproduto, (Categoria.id == Addproduto.categoria_id)).all()
    return render_template('produtos/index.html', produtos=produtos, marcas=marcas, categorias = categorias)


@app.route('/marca/<int:id>')
def get_marca(id):

    marca = Addproduto.query.filter_by(marca_id=id)
    marcas = Marca.query.join(Addproduto, (Marca.id == Addproduto.marca_id)).all()
    categorias = Categoria.query.join(Addproduto, (Categoria.id == Addproduto.categoria_id)).all()
    return render_template('produtos/index.html', marca = marca, marcas = marcas, categorias = categorias)


@app.route('/categoria/<int:id>')
def get_categoria(id):

    categoria = Addproduto.query.filter_by(categoria_id=id)
    categorias = Categoria.query.join(Addproduto, (Categoria.id == Addproduto.categoria_id)).all()
    marcas = Marca.query.join(Addproduto, (Marca.id == Addproduto.marca_id)).all()
    return render_template('produtos/index.html', categoria = categoria, categorias = categorias, marcas = marcas)


@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
    if'email' not in session:
        flash('Fazer login no sistema primeiro.', category='danger')
        return redirect(url_for('login'))

    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marca(name=getmarca)
        db.session.add(marca)
        flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addmarca'))
    return render_template('/produtos/addmarca.html', marcas='marcas')


@app.route('/updatemarca/<int:id>', methods=['GET', 'POST'])
def updatemarca(id):
    if'email' not in session:
        flash('Fazer login no sistema primeiro.', category='danger')
        return redirect(url_for('login'))

    updatemarca = Marca.query.get_or_404(id)
    marca = request.form.get('marca')
    if request.method == 'POST':
        updatemarca.name = marca
        flash('O fabricante foi atualizado com sucesso.', category='success')
        db.session.commit()
        return redirect(url_for('marcas'))
    return render_template('/produtos/updatemarca.html', title='Atualizar Fabricante', updatemarca = updatemarca)


@app.route('/deletemarca/<int:id>', methods=['POST'])
def deletemarca(id):

    marca = Marca.query.get_or_404(id)
    if request.method == 'POST':
        try:   
            db.session.delete(marca)
            db.session.commit()
            flash(f'A marca {marca.name} foi deletada com sucesso!', 'success')
        except IntegrityError:
            db.session.rollback()
            flash(f'Não foi possível deletar a marca {marca.name}. Existem produtos associados a ela.', 'danger')

        return redirect(url_for('admin'))
    
    flash(f'A marca {marca.name} não foi deletada!', 'warning')
    return redirect(url_for('admin'))
    


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if'email' not in session:
        flash('Fazer login no sistema primeiro.', category='danger')
        return redirect(url_for('login'))

    if request.method == "POST":
        getmarca = request.form.get('categoria')
        cat = Categoria(name=getmarca)
        db.session.add(cat)
        flash(f'A categoria {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('/produtos/addmarca.html')


@app.route('/updatecat/<int:id>', methods=['GET', 'POST'])
def updatecat(id):
    if'email' not in session:
        flash('Fazer login no sistema primeiro.', category='danger')
        return redirect(url_for('login'))

    updatecat = Categoria.query.get_or_404(id)
    categoria = request.form.get('categoria')
    if request.method == 'POST':
        updatecat.name = categoria
        flash('A categoria foi atualizada com sucesso.', category='success')
        db.session.commit()
        return redirect(url_for('categorias'))
    return render_template('/produtos/updatemarca.html', title='Atualizar Categoria', updatecat = updatecat)


@app.route('/deletecategoria/<int:id>', methods=['POST'])
def deletecategoria(id):

    categoria = Categoria.query.get_or_404(id)
    if request.method == 'POST':
        try:
            db.session.delete(categoria)
            db.session.commit()
            flash(f'A categoria {categoria.name} foi deletada com sucesso!', 'success')

        except IntegrityError:
            db.session.rollback()
            flash(f'Não foi possível deletar a marca {categoria.name}. Existem produtos associados a ela.', 'danger')

        return redirect(url_for('admin'))
    
    flash(f'A marca {categoria.name} não foi deletada!', 'warning')
    return redirect(url_for('admin'))


@app.route('/addproduto', methods=['GET', 'POST'])
def addproduto():
    if'email' not in session:
        flash('Fazer login no sistema primeiro.', category='danger')
        return redirect(url_for('login'))

    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    form = Addprodutos(request.form)
    if request.method=="POST":
     
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        description = form.description.data
        colors = form.colors.data
        marca = request.form.get('marca')
        categoria = request.form.get('categoria')

        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+".")

        addpro = Addproduto(name=name, price=price, discount=discount, stock=stock, description=description, colors=colors, marca_id=marca, categoria_id=categoria, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addpro)
        flash(f'Produto {name} foi cadastrada com sucesso', 'success')
        db.session.commit() # --> Responsável por salvar no banco de dados
        return redirect(url_for('admin'))
    
    return render_template('produtos/addproduto.html', title='Cadastrar Produtos', form=form, marcas = marcas, categorias = categorias)


@app.route('/updateproduto/<int:id>', methods=['GET', 'POST'])
def updateproduto(id):
    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    produto = Addproduto.query.get_or_404(id)
    form = Addprodutos(request.form)

    if request.method == 'POST':

        marca_id = request.form.get('marca') # Diferente dos demais, a marca e a categoria precisaram ser definidas dentro do POST
        categoria_id = request.form.get('categoria')

        produto.name = form.name.data
        produto.price = form.price.data
        produto.discount = form.discount.data
        produto.stock = form.stock.data
        produto.marca_id = marca_id
        produto.categoria_id = categoria_id
        produto.description = form.description.data
        produto.colors = form.colors.data

        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + produto.image_1))
                produto.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
            except:
                produto.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")

        
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + produto.image_2))
                produto.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+".")
            except:
                produto.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+".")

        
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + produto.image_3))
                produto.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+".")
            except:
                produto.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+".")

        db.session.commit()
        flash(f'O produto foi atualizado com sucesso', 'success')
        return redirect('/')

    form.name.data = produto.name
    form.price.data = produto.price
    form.discount.data = produto.discount
    form.stock.data = produto.stock
    form.description.data = produto.description
    form.colors.data = produto.colors

    return render_template('/produtos/updateproduto.html', title='Atualizar Produto', marcas=marcas, categorias=categorias, produto=produto, form=form)


@app.route('/deleteproduto/<int:id>', methods=['POST'])
def deleteproduto(id):

    produto = Addproduto.query.get_or_404(id)

    if request.method == 'POST':
        try:
            if produto.image_1:
                try:
                    os.unlink(os.path.join(current_app.root_path, "static/images/" + produto.image_1))
                    os.unlink(os.path.join(current_app.root_path, "static/images/" + produto.image_2))
                    os.unlink(os.path.join(current_app.root_path, "static/images/" + produto.image_3))
            
                except Exception as e:
                    print(f"Erro ao deletar o arquivo de imagem: {e}")
        
            db.session.delete(produto)
            db.session.commit()
            flash(f'O produto {produto.name} foi deletado com sucesso!', 'success')
        
        except Exception as e:
            db.session.rollback()
            flash(f'Ocorreu um erro ao deletar o produto {produto.name}.', 'danger')
            print(f"Erro no banco de dados ao deletar produto: {e}")

        return redirect(url_for('admin'))
    
    return redirect(url_for('admin'))