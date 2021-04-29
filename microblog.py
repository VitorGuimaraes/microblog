from app import app, db 
from app.models import User, Post

# Antes de executar, insira no terminal:
# export FLASK_APP=microblog.py 
# flask run (coloca o servidor no ar)

# Esse comando diz ao flask qual aplicação ele deve servir
# Se não for informado, o wsgi.py é importado e tenta identificar
# automaticamente um app (app) ou factory (create_app)
# Pode dar algum erro se tentar executar sem exportar a tag FLASK_APP

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}