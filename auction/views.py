from flask import Blueprint, render_template, url_for, redirect
from flask import request
from flask import session
from .models import Itemcreate


bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    Items = Itemcreate.query.all()
    return render_template('homepage.html', Items=Items)


@bp.route('/search')
def search():
    #get the search string from request
    if request.args['search']:
        watc = "%" + request.args['search'] + '%'
         #use filter and like function to search for matching destinations
        Items = Itemcreate.query.filter(Itemcreate.make.like(watc)).all()
        #render index.html with few destinations
        return render_template('homepage.html', Items=Items)
    else:
        return redirect(url_for('homepage.html'))

@bp.route('/homepage.html')
def index():
    Items = Itemcreate.query.all()
    return render_template('homepage.html', Items=Items)

@bp.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')



