from flask import Blueprint, render_template, redirect, url_for
from .models import Itemcreate, Comment
from .forms import CommentForm

watch_bp = Blueprint('watch', __name__, url_prefix='/watch')


@watch_bp.route('/<id>')
def itemdetails(id):
    watch = Itemcreate.query.filter_by(id=id).first()
    # create the comment form 
    cform= CommentForm() 
    return render_template('itemdetails.html', watch=watch, form=cform)


@watch_bp.route('/<id>/comment', methods = ['GET', 'POST'])  
def comment(id):  
  #here the form is created 
  form = CommentForm()  
  if form.validate_on_submit():  #this is true only in case of POST method
    print("Comment posted by the user:", form.text.data)  
  
  # in any case we go back to the same page.
  # notice the signature of url_for 
  return redirect(url_for('watch.itemdetails', id=id))
