from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField)
from wtforms.validators import InputRequired ##import validators from wtforms

class ContactForm(FlaskForm): ## creating the class contactForm with inheriting flaskform properties
    name = StringField('Name', validators=[InputRequired()])  ## StringField is the textfield and inputRequired is for input validation 
    email = StringField("E-mail", validators=[InputRequired()]) ## StringField is the textfield and inputRequired is for input validation 
    subject = StringField('Subject', validators=[InputRequired()]) ## StringField is the textfield and inputRequired is for input validation 
    msg = TextAreaField('Message', validators=[InputRequired()]) ## TextAreaField is the textfield and inputRequired is for input validation 