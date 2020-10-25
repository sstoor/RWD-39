from flask import Blueprint
from flask import Blueprint, render_template, url_for, redirect
from flask import request
from flask import session


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/search')
def search():
    #get the search string from request
    if request.args['search']:
        dest = "%" + request.args['search'] + '%'
         #use filter and like function to search for matching destinations
        destinations = Destination.query.filter(Destination.name.like(dest)).all()
        #render index.html with few destinations
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))