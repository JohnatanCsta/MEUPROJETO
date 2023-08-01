
# Aplicação Flask para iniciantes

O Flask é um framework web leve e minimalista em Python, ideal para iniciantes. Ele permite criar rapidamente aplicações web utilizando rotas simples e templates Jinja2. Sua comunidade ativa e ampla variedade de extensões facilitam o aprendizado e a adição de funcionalidades complexas sem complicações. O Flask oferece uma excelente porta de entrada para o desenvolvimento web em Python, tornando a criação de aplicações web uma experiência agradável e eficiente para iniciantes e programadores experientes.
## Licença

[MIT](https://choosealicense.com/licenses/mit/)
## Instalação

Passo 1: Instalar o Python  
Se você ainda não tiver o Python instalado em seu sistema, baixe e instale a versão mais recente em:.

```bash
  https://www.python.org/downloads/
```

Passo 2: Criar uma pasta  
Após a instalação do Python, abra o terminal (ou prompt de comando) crie uma pasta para o projeto:

```bash
  mkdir meuprojeto
  cd meuprojeto
```

Passo 3: Criar e Ativar o Ambiente Virtual  
No terminal, navegue até a pasta do seu projeto e crie um ambiente virtual usando o virtualenv:

```bash
  py -3 -m venv maquinavirtual
  maquinavirtual\Scripts\activate
```
Passo 4: Instalar o Flask  
Dentro do ambiente virtual, use o pip para instalar o Flask:

```bash
  pip install flask
```

Passo 5: Desenvolva seu Aplicativo Flask  
Agora você pode escrever o código do seu aplicativo Flask no arquivo "app.py".

```bash
  from flask import Flask

  app = Flask(__name__)
 
  @app.route('/')
  def index():
      return 'Olá, mundo!'
```

Passo 6: Iniciar a aplicação  
Após iniciar a aplicação, você receberá um link redirecionando a página web onde aparecerá suas modificações

```bash
  flask run
```
## Documentação

[Documentação do Python](https://docs.python.org/3/)  
[Documentação do Flask](https://flask.palletsprojects.com/en/2.3.x/)


## Autor

- [@johnatancsta](https://www.github.com/johnatancsta)