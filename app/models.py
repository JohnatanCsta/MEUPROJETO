from app import app, db

class ContatoModels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    conteudo = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'Contato {self.nome}'

class CadastroModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    sobrenome = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(60), nullable = False, unique = True )
    senha = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return 'Cadastro!'