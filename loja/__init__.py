from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///minhaloja.db" # --> caminho relativo (Por padrão, o Flask (e o SQLAlchemy com esta configuração) resolve caminhos relativos de arquivos de dados para o instance_path da aplicação, que é a pasta instance/.)
# configuração de uma chave secreta aleatória
app.config['SECRET_KEY'] = 'djfjfjajl'
# initialize the app with the extension
db = SQLAlchemy(app)
#criptografia de senhas
bcrypt = Bcrypt(app)

from loja.admin import rotas