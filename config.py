import os 

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY-key') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# A secret-key é usada para assinar o cookie de sessão com segurança e também
# em outras extensões da aplicação que precisem de segurança 

# SQLALCHEMY_DATABASE_URI define o tipo e local do banco de dados.

# SQLALCHEMY_TRACK_MODIFICATIONS notifica antes e depois que alterações são
# comitadas no banco de dados. 

