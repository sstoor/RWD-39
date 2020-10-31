#import flask - from the package import class
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .forms import ItemcreateForm

db=SQLAlchemy()

#create a function that creates a web application
# a web server will run this web application
def create_app():
  
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug=True
    app.secret_key='utroutoru'
    #set the app configuration data 
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///marketplace.sqlite'
    #initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)
    
    #initialize the login manager
    login_manager = LoginManager()
    
    #set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    #from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #importing views module here to avoid circular references
    # a commonly used practice.
    from . import views
    app.register_blueprint(views.bp)

    from . import Itemcreate
    app.register_blueprint(Itemcreate.itemcreate_bp)

    from . import auth
    app.register_blueprint(auth.bp)

    # Handle 404 Error
    @app.errorhandler(404)
    def handle_404_exception(e):
        return render_template('error.html', title='Page Not Found', msg=str(e))

    # Handle 500 Error
    @app.errorhandler(500)
    def handle_500_exception(e):
        return render_template('error.html', title="This page isn't working", msg=str(e))

    # Register general error handler
    @app.errorhandler(Exception)
    def handle__exception(e):
        return render_template('error.html', title='Something unexpected has happened', msg=str(e))

    return app



