from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
)
from .models import User
from .models import Itemcreate
from flask_sqlalchemy import SQLAlchemy
from auction.forms import ItemcreateFrom    
from . import db
#create a blueprint for iitem creation
itemcreate_bp = Blueprint('Itemcreate', __name__)
@bp.route('/addwatches', methods = ['GET', 'POST'])
def create():
print('Method type: ', request.method)
form = ItemcreateForm() 
if form.validate_on_submit():
print('Successfully added your item', 'success')
return render_template('auction/addwatches.html', form=form)
