import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY-key') or 'you-will-never-guess'

# A secret-key é usada para assinar o cookie de sessão com segurança e também
# em outras extensões da aplicação que precisem de segurança 