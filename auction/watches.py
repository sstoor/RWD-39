from flask import Blueprint, render_template
from .models import Watch, Itemcreate

watch_bp = Blueprint('watch', __name__, url_prefix='/watch')


@watch_bp.route('/<id>')
def itemdetails(id):
    watch = Itemcreate.query.filter_by(id=id).first()
    return render_template('itemdetails.html', watch=watch)
