from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title= ' sobre')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', title= ' projetos')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html', title= ' contatos')