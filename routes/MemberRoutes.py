from flask import Blueprint
from models.models import Member
from flask.json import jsonify

member = Blueprint('member', __name__, url_prefix="/member")

@member.route('/')
def index():
    return jsonify(data=[i.serialize for i in Member.query.all()])
