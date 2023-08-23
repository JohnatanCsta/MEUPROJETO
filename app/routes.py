from app import app, db, bcrypt
from flask import render_template,url_for, flash, redirect, request, session
from app.forms import Contato, Cadastro
import time
from app.models import ContatoModels, CadastroModel
from flask_bcrypt import check_password_hash

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
    return render_template('projeto.html', title ='Projeto') 

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    print('Acessou a rota de cadastro')
    cadastro = Cadastro()
    if cadastro.validate_on_submit():
        try:
            nome = cadastro.nome.data
            sobrenome = cadastro.sobrenome.data
            email = cadastro.email.data
            senha = cadastro.senha.data
            telefone = cadastro.telefone.data
            rua = cadastro.rua.data
            bairro = cadastro.bairro.data
            cidade = cadastro.cidade.data
            estado = cadastro.estado.data
            cpf = cadastro.cpf.data
            hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
            novo_cadastro = CadastroModel(nome=nome, sobrenome=sobrenome, email=email, telefone=telefone, rua=rua, bairro=bairro, cidade=cidade, estado=estado, cpf=cpf, senha=hash_senha)
            db.session.add(novo_cadastro)
            db.session.commit()
            flash('Seu cadastro foi realizado com sucesso!')
        except Exception as e:
            flash('Ocorreu um erro ao cadastrar! Entre em contato com o suporte: adm@admin.com')
            print(str(e))
    return render_template('cadastro.html', titulo='Cadastro', cadastro=cadastro)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        user = CadastroModel.query.filter_by(email=email).first()
        print(check_password_hash(user.senha, senha))
        if user and check_password_hash(user.senha, senha):
            session['email'] = user.email
            session['nome'] = user.nome
            session['sobrenome'] = user.sobrenome
            session['telefone'] = user.telefone
            session['rua'] = user.rua
            session['bairro'] = user.bairro
            session['cidade'] = user.cidade
            session['estado'] = user.estado
            session['senha'] = user.senha
            flash('Seja bem vindo')
            return redirect(url_for('index'))

        else:
            flash('Senha ou e-mail incorreto!')
    return render_template('login.html', titulo='Login')

@app.route('/sair')
def sair():
    session.pop('email', None)
    session.pop('nome', None)
    session.pop('sobrenome', None)
    session.pop('telefone', None)
    session.pop('rua', None)
    session.pop('bairro', None)
    session.pop('cidade', None)
    session.pop('estado', None)
    session.pop('cpf', None)
    session.pop('senha', None)
    return redirect(url_for('login'))

@app.route('/editar', methods=['POST', 'GET'])
def editar():
    if 'email' not in session:
        return redirect(url_for('login'))
    usuario = CadastroModel.query.filter_by(email = session['email']).first()
    if request.method == 'POST':
        usuario.nome = request.form.get('nome')
        usuario.sobrenome = request.form.get('sobrenome')
        usuario.telefone = request.form.get('telefone')
        usuario.rua = request.form.get('rua')
        usuario.bairro = request.form.get('bairro')
        usuario.cidade = request.form.get('cidade')
        usuario.estado = request.form.get('estado')
        usuario.email = request.form.get('email')
        senha = request.form.get('senha')
        usuario.senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        db.session.commit()
        session['email'] = usuario.email  
        session['nome'] = usuario.nome
        session['sobrenome'] = usuario.sobrenome
        session['telefone'] = usuario.telefone
        session['rua'] = usuario.rua
        session['bairro'] = usuario.bairro
        session['cidade'] = usuario.cidade
        session['estado'] = usuario.estado
        session['senha'] = usuario.senha
        db.session.commit()

        flash('Seus dados foram atualizados com sucesso!')
        return redirect(url_for('editar'))
    return render_template('editar.html', titulo= 'Editar', usuario = usuario)

@app.route('/excluir', methods=['GET'])
def excluir():
    if 'email' not in session:
        return redirect(url_for('login'))

    usuario = CadastroModel.query.filter_by(email = session['email']).first()
    db.session.delete(usuario)
    db.session.commit()
    session.clear()

    flash('Sua conta foi excluída com sucesso!')
    return redirect(url_for('cadastro'))

@app.route('/projeto1')
def projeto1():
    return render_template('projeto1.html', title ='Projeto Um') 