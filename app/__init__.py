from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Migrate é um framework que permite realizar alterações no schema do BD
# Schema são as tabelas, colunas, tipos de dados, índices, chaves...

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models 