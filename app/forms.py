from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, PasswordField
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
    enviar = SubmitField('Enviar')