from flask import Blueprint

bp = Blueprint('login', __name__, url_prefix='/')


@bp.route('/')
def index():
    pass
