from datetime import datetime
from app import db


# Bancos de dados relacionais só conseguem realizar buscas eficientes em 
# atributos indexados. Nesse caso iremos fazer buscas por username e email,
# portanto, essas colunas receberão index=True
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # backref: é uma forma de adicionar mais uma propriedade à classe Post
    # lazy=dynamic: retorna uma query que pode ser refinada antes de trazer os itens,
    # como ordenação por data
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Para tornar essa classe amigável para debugar no console
    # Método que printa a classe
    def __repr__(self):
        return '<User {}>'.format(self.username)

# *** Migrations ***
# O que fizemos até aqui foi definir um usuário em uma classe, mas esse modelo
# só existe como um objeto Python. 
# Após modelar o banco em classes python, inicialize o framework de migrações,
# assim podemos aplicar a migração da tabela User
# flask db init
# Esse comando vai criar o diretório migrations, contendo scripts python que
# descrevem as alterações realizadas no banco de dados
# Você precisa tratar o conteúdo desse diretório como parte da aplicação. 
# Isso significa que você deve adicionar o conteúdo desse diretório ao repositório
# do projeto

# Após criar o repositório migrates com o comando acima, você está pronto para
# criar sua primeira migration
# flask db migrate -m "user table"
# As migrações ficam em migrations/versions 
# As versões possuem uma função upgrade, que contém as alterações que foram realizadas
# e uma função downgrade, que desfaz as alterações

# Histórico de migrations
# flask db history

# Versão atual da migration
# flask db current

# Reverte para a migration anterior
# flask db downgrade 

# Atualiza a para versão mais recente (head)
# flask db upgrade 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # index: necessário pois vamos filtrar do mais novo para mais antigo
    # Vamos usar utcnow agora. Posteriormente vamos ver como lidar com data
    # e tempo em um servidor
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) 
    # Foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

# gravar quem é o autor do post