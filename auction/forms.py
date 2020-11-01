
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}

# creates the login information


class LoginForm(FlaskForm):
		user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
		password = PasswordField("Password", validators=[InputRequired('Enter user password')])
		submit = SubmitField("Login")

 # this is the registration form


class RegisterForm(FlaskForm):
		user_name = StringField("User Name", validators=[InputRequired()])
		email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])

		# add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field

		# linking two fields - password should be equal to data entered in confirm
		password = PasswordField("Password", validators=[InputRequired(), EqualTo('confirm', message="Passwords should match")])
		confirm = PasswordField("Confirm Password")

		# submit button
		submit = SubmitField("Register")


class ItemcreateForm(FlaskForm):
	make = TextAreaField('Make', validators=[InputRequired()])
	model = TextAreaField('Model', validators=[InputRequired()])
	movement = TextAreaField('Movement', validators=[InputRequired()])
	starting_bid = TextAreaField('Starting Bid', validators=[InputRequired()])
	year = TextAreaField('Year', validators=[InputRequired()])
	condition = TextAreaField('Condition', validators=[InputRequired()])
	description = TextAreaField('Description', validators=[InputRequired()])
	# adding two validators, one to ensure input is entered and other to check if the 
	# description meets the length requirements
	image = FileField('Destination Image', validators=[FileRequired(message='Image can not be empty'), FileAllowed(ALLOWED_FILE, message='Only supports png, jpg, JPG, PNG')])
	submit = SubmitField("Create")

class CommentForm(FlaskForm):
		text = TextAreaField('Comment', [InputRequired()])
		submit = SubmitField('Create')
