from flask_sqlalchemy import SQLAlchemy
import datetime
import json

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """ Define a base way to jsonify models, dealing with datetime objects """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


def to_json(inst, cls):
    """Jsonify the sql alchemy query result."""
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return d


class Member(BaseModel, db.Model):
    """Member: Miembros de GUMus"""
    __tablename__ = 'member'

    id          = db.Column(db.Integer, primary_key = True)
    name        = db.Column(db.String)
    lastname    = db.Column(db.String)
    meetups     = db.relationship("Meetup")

    @property
    def serialize(self):
        return to_json(self, self.__class__)

class Meetup(BaseModel, db.Model):
    """Meetup: Charlas que den los usuarios"""
    __tablename__ = 'meetup'

    id          = db.Column(db.Integer, primary_key = "True")
    title       = db.Column(db.String)
    description = db.Column(db.String)
    #place      = 
    member_id   = db.Column(db.Integer, db.ForeignKey('member.id'))

    @property
    def serialize(self):
        return to_json(self, self.__class__)