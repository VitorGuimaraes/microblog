from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Qual a diferença entre DataRequired e InputRequired?

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# https://www.youtube.com/watch?v=jR2aFKuaOBs