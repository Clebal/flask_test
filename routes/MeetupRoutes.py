from flask import Blueprint
from models.models import Meetup
from flask.json import jsonify

meetup = Blueprint('meetup', __name__, url_prefix="/meetup")

@meetup.route('/')
def index():
    return jsonify(data=[i.serialize for i in Meetup.query.all()])