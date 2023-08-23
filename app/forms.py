from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, PasswordField, TelField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect


class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    conteudo = TextAreaField('conteudo')
    enviar = SubmitField('enviar')

class Cadastro(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    sobrenome = StringField('sobrenome', validators=[DataRequired()])
    email = EmailField('email',validators=[DataRequired()])
    senha = PasswordField('senha',validators=[DataRequired()])
    telefone = TelField('nome', validators=[DataRequired()])
    rua = StringField('rua', validators=[DataRequired()])
    bairro = StringField('bairro', validators=[DataRequired()])
    cidade = StringField('cidade', validators=[DataRequired()])
    estado = StringField('estado', validators=[DataRequired()])
    cpf = StringField('estado', validators=[DataRequired()])
    enviar = SubmitField('Enviar')