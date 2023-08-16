from app import app, db
from flask import render_template,url_for, flash, redirect, request, session
from app.forms import Contato, Cadastro
import time
from app.models import ContatoModels, CadastroModel

@app.route('/')
def index():
    return render_template('index.html', title = 'Inicio')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title ='Sobre')

@app.route('/contato',methods=['GET','POST'])
def contato():
    formulario = Contato()
    if formulario.validate_on_submit():
        flash('Seu formulário foi enviado com sucesso!!')
        nome = formulario.nome.data
        email = formulario.email.data
        conteudo = formulario.conteudo.data
        novo_contato = ContatoModels(nome = nome, email = email, conteudo = conteudo)
        db.session.add(novo_contato)
        db.session.commit()

    return render_template('contato.html', title = 'Contato', formulario = formulario)

@app.route('/projetos')
def projeto():
    return render_template('projeto.html', title ='Projetos') 

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    cadastro = Cadastro()
    if cadastro.validate_on_submit():
        try:
            nome = cadastro.nome.data
            sobrenome = cadastro.sobrenome.data
            email = cadastro.email.data
            senha = cadastro.senha.data

            novo_cadastro = CadastroModel(nome = nome, sobrenome = sobrenome, email=email, senha=senha)
            db.session.add(novo_cadastro)
            db.session.commit()
            flash('Seu cadastro foi realizado com sucesso!')
        except Exception as e:
            flash('Ocorreu um erro ao cadastrar! Entre em contato com o suporte: adm@admin.com')
            print(str(e))

    return render_template('cadastro.html', title = 'Cadastro', cadastro = cadastro)

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        user = CadastroModel.query.filter_by(email = email, senha = senha).first()
        if user and user.senha == senha:
            session['email']  = user.id
            flash('Seja bem vindo')
            time.sleep(2)
            return redirect(url_for('index'))
        else:
            flash('Senha ou e-mail incorreto!')


    return render_template('login.html', title = 'Login')