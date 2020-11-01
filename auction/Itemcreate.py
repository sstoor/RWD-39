from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from .models import User
from .models import Itemcreate
from flask_sqlalchemy import SQLAlchemy
from .forms import ItemcreateForm    
from . import db
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

#create a blueprint for iitem creation
itemcreate_bp = Blueprint('Itemcreate', __name__)

#@itemcreate_bp.route('/<id>')
#def show(id):



def check_upload_file(form):
    # get file data from form
    fp = form.image.data
    filename = fp.filename
    # # get the current path of the module file… store image file relative to this path
    BASE_PATH = os.path.dirname(__file__)
    # #upload file location – directory of this file/static/image
    upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
    # # store relative path in DB as image location in HTML is relative
    db_upload_path = '/static/image/'+ secure_filename(filename)
    # # save the file and return the db upload path
    fp.save(upload_path)
    return db_upload_path

@itemcreate_bp.route('/addwatches', methods=['GET', 'POST'])
@login_required
def create():
    #print('Method type: ', request.method)
    form = ItemcreateForm() 
    if form.validate_on_submit():
        db_file_path = check_upload_file(form)
        Item = Itemcreate(make=form.make.data, description=form.description.data, 
                                     image=db_file_path, model=form.model.data, 
                                     movement=form.movement.data, year=form.year.data, 
                                     condition=form.condition.data, starting_bid=form.starting_bid.data)
        
        db.session.add(Item)
        db.session.commit()
    
        print('Successfully added your item', 'success')

        return render_template('homepage.html')

    else:
        return render_template('addwatches.html', form=form)


@itemcreate_bp.route('/<id>/comment', methods = ['GET', 'POST'])
@login_required
def comment(id):
    form = CommentForm()
    #get the destination object associated to the page and the comment
    destination_obj = Itemcreate.query.filter_by(id=id).first()
    
    if form.validate_on_submit():
        #read the comment from the form
        comment = Comment(text=form.text.data, 
        destination=destination_obj, user = current_user)
        #here the back-referencing works - comment.destination is set
        # # and the link is created
        #db.session.add(comment)
        db.session.commit()
        
        
        
        print('Your comment has been added', 'success')
    # using redirect sends a GET request to destination.show
    return redirect(url_for('destination.show', id=id))