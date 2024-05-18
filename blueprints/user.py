from flask import Blueprint
bp = Blueprint('user', __name__, url_prefix='/user')


# /user/student
@bp.route('/student')
def student():
    pass