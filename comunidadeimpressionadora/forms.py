from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError #validadores de campos
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usúario', validators=[DataRequired(message="Digite um nome de usuário válido")]) #datarequirred quando é um dado obrrigatório para seguir
    email = StringField('E-mail', validators=[DataRequired(), Email(message="Digite um endedreço de e-mail válido")])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20,message="Digite um valor para senha de 6 a 20 caracterres")])
    confirmacao_senha = PasswordField('Confirmação da senha', validators=[DataRequired(message="Senha diferente da preenchida anteriormente"), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')
# tudo quee precisa ser validade no site precisa do parametro validators=[]

    #Função que valida se o email criado já existe
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadestre-se com outro email ou faça login para continuar')

# Liberar login de usuario no terminal: pip install flask-login


# Para validação da senha criada no formulario de criar na conta e loin, a validação é feita posteriormente no banco de dados
class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email(message = "Digite um endedreço de e-mail válido")])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20, message= "Senha diferente da preenchida anteriormente")])
    botao_submit_login = SubmitField('Fazer login')
    lembrar_dados = BooleanField('Lembrar dados de acesso') #botão de esqueci senha site
#os nomes de botões de criar conta e logar precisam ser diferentes pois estarão na mesma página do site

# Criptografar senhas de usuarios, deve ser feito no terminal
#pip install flask-bcrypt
#Deve ser criada uma instancia do bcrypt no arquivo init

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usúario', validators=[DataRequired(message="Digite um nome de usuário válido")])
    email = StringField('E-mail', validators=[DataRequired(), Email(message="Digite um endedreço de e-mail válido")])
    foto_perfil = FileField('Atualizar foto de perfil', validators=[FileAllowed(['jpg', 'png'])]) # permissão para editar foto de perfil

    curso_excel = BooleanField('Excel Impressionador')
    curso_vba = BooleanField('VBA Impressionador')
    curso_powerbi = BooleanField('Power BI Impressionador')
    curso_python = BooleanField('Python Impressionador')
    curso_ppt = BooleanField('Apresentações Impressionadoras')
    curso_sql = BooleanField('SQL Impressionador')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com outro email. Cadastre outro email.')

class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Posto')