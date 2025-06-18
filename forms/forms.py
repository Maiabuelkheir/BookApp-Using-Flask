from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, DecimalField, SubmitField , FileField,PasswordField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange, Optional ,EqualTo, Email

class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired(), Length(max=100)])
    publish_date = DateField('Publish Date', format='%Y-%m-%d', validators=[DataRequired()])
    add_to_site_at = DateField('Add to Site At', format='%Y-%m-%d', validators=[DataRequired()])
    author = SelectField('Author', choices=[], coerce=int, validators=[Optional()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)], places=2)
    image = FileField('Book Cover', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    appropriate = SelectField('Appropriate for Age', choices=[('under_8', 'Under 8'), ('8_15', '8-15'), ('adults', 'Adults')])
    submit = SubmitField('Add Book')


class AuthorForm(FlaskForm):
    name = StringField('Author Name', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Add Author')


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Login")