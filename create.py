from application import db
from application.models import Fighters


db.drop_all()
db.create_all()
