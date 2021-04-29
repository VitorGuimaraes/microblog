from app import db 
from app.models import User, Post 


u = User(username='John', email='john@example.com')

db.session.add(u) # Adiciona o usuário no banco de dados
db.session.commit() # comita as alterações

u = User(username='Susan', email='susan@example.com')
db.session.add(u)
db.session.commit()

# query na tabela Users  
users = User.query.all() 
print(users)

for u in users:
    print(u.id, u.username, u.email)

# query user pela primary key
u = User.query.get(1) # primary key 1 (John)
print(u)

# Criando um post 
p = Post(body='My first post', author=u) 
db.session.add(p)
db.session.commit()

# show all posts from John
posts = u.posts.all()
print(posts)

u = User.query.get(2) # primary key 2 (Susan)
print(u.posts.all())

# all posts of the database
posts = Post.query.all()
for p in posts:
    print(p.id, p.author.username, p.body)

# get a list of users and sort them alphabetically in decreasing order
users = User.query.order_by(User.username.desc()).all()
print(users)


# delete objects
users = User.query.all()
for u in users:
    db.session.delete(u)

posts = Post.query.all()
for p in posts: 
    session.db.delete(p)