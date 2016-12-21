from flask_mongoengine import MongoEngine
from datetime import datetime

db = MongoEngine()


class User(db.Document):
    username = db.StringField(required=True, max_length=64)
    password = db.StringField(required=True, max_length=128)
    email = db.StringField(max_length=128)
    description = db.StringField(max_length=1024)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __unicode__(self):
        return self.username


class Post(db.Document):
    title = db.StringField(required=True, max_length=64)
    content = db.StringField(required=True)
    author = db.ReferenceField(User)
    tags = db.ListField(db.StringField(max_length=32))
    status = db.IntField(required=True)
    create_time = db.DateTimeField(default=datetime.now)
    modify_time = db.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.title

    meta = {
        'ordering': ['-create_time']
    }

