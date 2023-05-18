from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
import email_validator
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class regform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2, max = 20) ])
    email = StringField('Email',  validators =[DataRequired(),Email() ])
    password = PasswordField('Password', validators=[DataRequired()])
    confpassword = PasswordField('ConfPassword', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class loginform(FlaskForm):
    
    email = StringField('Email or Username',  validators =[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remeber Me')

    submit = SubmitField('Login')
