from peewee import *
db = SqliteDatabase('db/landingpage.db')
class User(Model):
    username = CharField()
    passwd = CharField()
    role = CharField()
    class Meta:
        database = db # This model uses the database.

class Nav(Model):
    title = CharField()
    url = CharField()
    class Meta:
        database = db # This model uses the database.

class Banner(Model):
    title = CharField()
    text = CharField()
    img = CharField()
    class Meta:
        database = db # This model uses the database.

class Document(Model):
    title = CharField()
    text = CharField()
    img = CharField()
    url = CharField()
    class Meta:
        database = db # This model uses the database.

class Task(Model):
    title = CharField()
    icon = CharField()
    text = CharField()
    users = CharField()
    status = CharField()
    url = CharField()
    class Meta:
        database = db # This model uses the database.

class Sample(Model):
    title = CharField()
    icon = CharField()
    text = CharField()
    url = CharField()
    class Meta:
        database = db # This model uses the database.

class Tool(Model):
    title = CharField()
    icon = CharField()
    text = CharField()
    url = CharField()
    class Meta:
        database = db # This model uses the database.


class Video(Model):
    title = CharField()
    icon = CharField()
    text = CharField()
    url = CharField()
    class Meta:
        database = db # This model uses the database.


class Community(Model):
    title = CharField()
    icon = CharField()
    url = CharField()
    class Meta:
        database = db # This model uses the database.
