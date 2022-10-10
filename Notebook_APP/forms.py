from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from notebook_app.models import User


class SearchForm(FlaskForm):
	searched = StringField('Search', validators=[DataRequired()])
	searchBtn = SubmitField('Search')


class UpdateNoteForm(FlaskForm):
	category = StringField('Category', validators=[DataRequired()])
	notes = TextAreaField('Notes', validators=[DataRequired()])
	image = FileField('Add note image', validators=[FileAllowed(['jpg', 'png'])])
	updateNoteBtn = SubmitField('Update')
	

class NewCategoryForm(FlaskForm):
	categories_name = StringField('Add new category here', validators=[DataRequired()])
	image = FileField('Add note image', validators=[FileAllowed(['jpg', 'png'])])
	submitCategoryUpdateBtn = SubmitField('SAVE')


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
	confirm_pasword = PasswordField('Confirm password', validators=[EqualTo('password', 'Passwords must be equal'), DataRequired()])
	RegisterBtn = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('This username is taken. Please choose a different one')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('This email is taken. Please choose a different one')


class LoginForm(FlaskForm):
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	loginBtn = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("Email", validators=[DataRequired(), Email()])
	updateAccBtn = SubmitField('Update')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('This email is taken. Please choose a different one')