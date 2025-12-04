from flask import render_template, session, request, url_for, flash,redirect, current_app
from loja import db, app
from loja.produtos.models import Addproduto


def M_Dicionarios(dic1, dic2):
    if isinstance(dic1, list) and isinstance(dic2, list):
        return dic1 + dic2
    elif isinstance(dic1, dict) and isinstance(dic2, dict):
        return dict(list(dic1.items()) + list(dic2.items()))
    return False

@app.route('/addCart', methods=['POST'])
def AddCart():
    try:
        produto_id = request.form.get('produto_id')
        
        try:
            quantity = int(request.form.get('quantity'))
        except ValueError:
            flash('Quantidade inválida.', 'danger')
            return redirect(request.referrer)
            
        colors = request.form.get('colors')
        produto = Addproduto.query.filter_by(id = produto_id).first()

        if produto and produto_id and quantity > 0 and colors and request.method == "POST":
            
            DicItens = {produto_id:{
                'Nome': produto.name, 
                'Preço': produto.price, 
                'Desconto': produto.discount, 
                'Cor': colors, 
                'Quantidade': quantity, 
                'Image': produto.image_1
            }}

            if 'LojainCarrinho' in session:
                # # Se o carrinho já existe, mescla o novo item (DicItens) no carrinho existente
                session['LojainCarrinho'].update(DicItens)
                flash('O produto foi adicionado/atualizado no carrinho!', 'success')

                if produto_id in session['LojainCarrinho']:
                    print('ESTE PRODUTO JÁ EXISTE NO CARRINHO.')
                else:
                    session['LojainCarrinho'] = M_Dicionarios(session['LojainCarrinho'], DicItens)
                    return redirect(request.referrer)
            else:
                #Se o carrinho não existe, cria-o
                session['LojainCarrinho'] = DicItens
                flash(f'O produto {produto.name} foi adicionado ao seu novo carrinho!', 'success')
                
    except Exception as e:
        print(e)
        flash('Ocorreu um erro ao adicionar o produto ao carrinho.', 'danger')
    finally:
        return redirect(request.referrer)