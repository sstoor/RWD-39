from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 

from auction.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from flask_sqlalchemy import SQLAlchemy
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required, logout_user
from auction.forms import ItemcreateFrom    
from . import db


#create a blueprint
bp = Blueprint('auth', __name__)


# this is the hint for a login function
@bp.route('/login', methods=['GET', 'POST'])
def login(): #view function
     print('In Login View function')
     login_form = LoginForm()
     error=None
     if(login_form.validate_on_submit()==True):
         user_name = login_form.user_name.data
         password = login_form.password.data
         u1 = User.query.filter_by(name=user_name).first()
         if u1 is None:
             error='Incorrect user name'
         elif not check_password_hash(u1.password_hash, password): # takes the hash and password
             error='Incorrect password'
         if error is None:
             login_user(u1)
             nextp = request.args.get('next') #this gives the url from where the login page was accessed
             print(nextp)
             if next is None or not nextp.startswith('/'):
                 return redirect(url_for('index'))
             return redirect(nextp)
         else:
             flash(error)
     return render_template('user.html', form=login_form, heading='Login')



@bp.route('/logout')
@login_required
def logout():
    logout_user()
   
    return 'you have been logged out'




@bp.route('/register', methods = ['GET', 'POST'])
def register():
    register_form_instance = RegisterForm()

    if register_form_instance.validate_on_submit():

        #grab details from form
        username = register_form_instance.user_name.data
        email = register_form_instance.email_id.data
        pwd = register_form_instance.password.data
        

        #check if username is original
        u = User.query.filter_by(name=username).first() # will return a user object
    
        if u:
            flash('This usernmae is already being used, please log In')
            return 'This user already exists, please login here'
        
        pwd_hash = generate_password_hash(pwd)
        new_user = User(name=username, emailid=email, password_hash=pwd_hash)


        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))

   # else:
    #    return render_template('register.html', form=register_form_instance, heading = 'Register')
        





        #if the username is unique, create a new user and commit to databsse



        
        
        return redirect(url_for('authentication.login'))
    
    
    return render_template('authentication/register.html', form=register_form_instance)

