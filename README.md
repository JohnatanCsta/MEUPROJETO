
# Aplicação Flask para iniciantes

O projeto "Meu Primeiro Blog com Flask" é um excelente ponto de partida para iniciantes que desejam aprender a desenvolver aplicações web utilizando o framework Flask em Python. Flask é uma estrutura leve e flexível que permite a criação rápida de aplicações web, tornando-o ideal para quem está dando os primeiros passos no desenvolvimento web.

Neste projeto, os participantes terão a oportunidade de construir um blog simples, onde poderão criar, editar e excluir postagens, além de visualizar os posts existentes. Serão abordados conceitos fundamentais, como rotas, templates, formulários e interações com um banco de dados para armazenar as postagens.


## Preparando o ambiente de desenvolvimento

Primeiro passo:
Crie uma pasta para o seu projeto:
```bash
mkdir meuprojeto
cd meuprojeto
```
Segundo passo: criar máquina virtual
```bash
py -3 -m venv nomedamaquinavirtual
```
Terceiro passo: ativar a máquina virtual no windows
```bash
nomedamaquinavirtual\Scripts\activate
```
Quarto passo: instalar o flask
```bash
pip install flask
```
Quinto passo: Para instalar as dependencias desse projeto, use o comando abaixo:
```bash
pip install -r requirements.txt
```
Sexto passo: Se você aprimorou o projeto, contribua adicionando as dependencias que utilizou com o comando abaixo:
```bash
pip freeze > requirements.txt
```
No terminal, na pasta do seu projeto, execute o seguinte comando para criar uma pasta para as migrações:
```bash
flask db init
```
Isso criará uma pasta chamada migrations onde as migrações serão armazenadas.
Agora você pode usar o seguinte comando para gerar uma migração baseada nos modelos que você definiu:
```bash
flask db migrate -m "Nome da Migração"
```
Resumindo:
```bash flask db init ``` - Uma vez para inicializar o sistema de migração.
```bash flask db migrate ```- Sempre que você fizer alterações em seus modelos.
```bash flask db upgrade ``` - Sempre que você quiser aplicar as migrações pendentes ao banco de dados.
## Autores

- [@JohnatanCsta](https://www.github.com/JohnatanCsta)

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
Escrito por Johnatan Medeiros