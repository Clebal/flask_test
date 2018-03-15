from models.models import db
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
 
from routes.MemberRoutes import member
from routes.MeetupRoutes import meetup

app = Flask(__name__)
migrate = Migrate(app, db)

# Warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

POSTGRES = {
    'user': 'clebal',
    'pw': '',
    'db': 'gumus',
    'host': 'localhost',
    'port': '5432',
}

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DB_USER:PASSWORD@HOST/DATABASE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['DEBUG'] = True

# Registrar blueprints
app.register_blueprint(member)
app.register_blueprint(meetup)


db.init_app(app)

if __name__ == '__main__':
    app.run()