from flask import Flask
from flask_sqlalchemy import SQLAlchemy # < banco de dados para o site, deve ser instalado no terminal antes
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__) #inicializa o site



app.config['SECRET_KEY'] = '7c24813ac22aefb2f57095c1782d6772+' #Código de segurrarnça do site. Ir em terminar, python, 'import secrerts' / secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db' # caminho local ao banco de dados no nosso computador

database = SQLAlchemy(app) # cria o banco de dados
bcrypt = Bcrypt(app) # criptografia para senhas
login_manager = LoginManager(app) # necessario para login site
login_manager.login_view = 'login' #sempre que for direcionado sem estar logado, automaticamente direciona para a tela de login
login_manager.login_message_category = 'alert-info' # alerta em caso de não estar logado

from comunidadeimpressionadora import routes # Executa o arquivo para colocar o link no ar