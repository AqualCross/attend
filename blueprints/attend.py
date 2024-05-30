from flask import Blueprint
from time import time
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Student

bp = Blueprint('student', __name__, url_prefix='/attend')

attendance_request = {}

