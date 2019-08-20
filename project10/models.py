import datetime
import config

from peewee import *

DATABASE = SqliteDatabase('todos.sqlite')

class Todo(Model):
    name = CharField()
    edited = BooleanField(default=False)
    completed = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(null=True, default=None)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Todo], safe=True)
    DATABASE.close()