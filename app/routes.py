from app import app
from flask import render_template

@app.routes('/')
def index():
    return render_template('index.html', title = 'Inicio')

@app.routes('/sobre')
def sobre():
    return render_template('sobre.html', title = 'Sobre')

@app.routes('/contato')
def contato():
    return render_template('contato.html', title = 'Contato')