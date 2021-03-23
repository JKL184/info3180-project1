from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from wtforms import StringField,TextAreaField,SelectField


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    room = StringField('No. of Rooms', validators=[DataRequired()])
    bathroom = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    proptype=SelectField(u'Property Type' ,choices=[('Apartment','Apartment'),('House','House')])
    desc= TextAreaField('Description', validators=[DataRequired()])
    photo=FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png'],'Images only!')])