from datetime import date, datetime
import re
from time import time
from peewee import *

db = SqliteDatabase('db.db')

class tasks(Model):

    id = AutoField()
    task = CharField()
    date = DateTimeField()
    done = BooleanField()

    class Meta:
        database = db

def added(text, date, done):
    
    date = str(date)
    date = date[:date.index('.')]
    row = tasks(task=text, date=date, done=done)
    row.save()
    
# tasks.create_table()