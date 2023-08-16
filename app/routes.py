from app import app, db
from flask import render_template,url_for, flash, redirect, request
from app.forms import Contato
import time
from app.models import ContatoModels

@app.route('/')
def index():
    return render_template('index.html', title = 'Inicio')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title ='Sobre')

@app.route('/contato',methods=['GET','POST'])
def contato():
    dados_formulario = None
    formulario = Contato()
    if formulario.validate_on_submit():
        flash('Seu formulário foi enviado com sucesso!!')
        nome = formulario.nome.data
        email = formulario.email.data
        conteudo = formulario.conteudo.data
        novo_contato = ContatoModels(nome = nome, email = email, conteudo = conteudo)
        db.session.add(novo_contato)
        db.session.commit()

    return render_template('contato.html', title = 'Contato', formulario = formulario, dados_formulario = dados_formulario)

@app.route('/projetos')
def projeto():
    return render_template('projeto.html', title ='Projetos') 

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', title = 'Cadastro')

@app.route('/login')
def login():
    return render_template('login.html', title = 'Login')