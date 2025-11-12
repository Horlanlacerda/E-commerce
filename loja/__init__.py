from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads
import os


# Define o caminho raiz (root pah) do projeto de forma absoluta e confiável
basedir = os.path.abspath(os.path.dirname(__file__))
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

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
# patch_request_class(app) --> Não funciona para versões recentes do werkzeug

from loja.admin import rotas
from loja.produtos import rotas