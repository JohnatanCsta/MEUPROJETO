from flask_wtf import FlaskForm
from wtforms import StringField, EmailFild, TextAreaField
from wtforms.validators import DataRequired

class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailFild('email', validators=[DataRequired()])
    conteudo = TextArealFild('conteudo')