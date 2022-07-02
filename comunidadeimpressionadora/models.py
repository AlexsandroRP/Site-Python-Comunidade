from comunidadeimpressionadora import database, login_manager
from datetime import datetime
from flask_login import UserMixin

#Função que carrega o usuário
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False) #Campo não pode ser falso
    senha = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True) # Somente um usuario por email
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True) # relaciona com outra tabela do banco
    cursos = database.Column(database.String, nullable=False, default='Não Informado')

    def contar_posts(self):
        return len(self.posts)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False) # Textos grandes usa text ao inves de string
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False) # relaciona com a tabela de usuario. Tem que estar em minuscula

""" 
Criando o database após criação das colunas:
    Python console, 'from main import database',
    'from models import Usuario, Post'. Por fim: database,create_all()

Criando usuário e importando pro database:

    usuario = Usuario(username="Alex", email="alexsdsads@gmail.com", senha="sdds744fdsfd")
    usuario2 = Usuario(username="Sandro", email="alexsdsadsads@gmail.com", senha="s744fdsfd")

Importando para o banco:

    database.session.add(usuario)
    database.session.add(usuario2)

Registrar no banco de dados (adciona todos os usuarios de uma vez)

    database.session.commit()
    
Informar todos os usuarios dentro da tabela (serve para os posts tmb, só trocar o nome:

    Usuario.query.all()

Pegar infos do usuario:

    usuario_teste = Usuario.query.first()
    usuario_teste.email (pegar somente o email nesse exemplo)

Filtrando por email:

    usuario_alex2 = Usuario.query.filter_by(email='alexsdsadsads@gmail.com').first()
    usuario_alex2

Criando posts:
    
    post1 = Post(titulo="Post Alex", corpo="Primeiro post do site", id_usuario=1)
    
    database.session.add(post1)
    
    database.session.commit()

    Post.query.all()

    post1 = Post.query.first()
    
    post1

    post1.titulo
    
Deletando banco de dados:

    database.drop_all()    
"""

