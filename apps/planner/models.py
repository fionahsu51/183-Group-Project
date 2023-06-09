"""
This file defines the database models
"""

import datetime
import random
from py4web.utils.populate import FIRST_NAMES, LAST_NAMES, IUP
from .common import db, Field, auth
from pydal.validators import *

def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_username():
    return auth.current_user.get('username') if auth.current_user else None

def get_user():
    return auth.current_user.get('id') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()


### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later

db.define_table(
    'project',
    Field('name', requires=IS_NOT_EMPTY()),
    Field('color', requires=[IS_NOT_EMPTY(), IS_IN_SET(['Gray', 'Blue', 'Light blue', 'Green', 'Teal', 'Yellow', 'Red'])]),
    auth.signature
)
db.project.id.readable = db.project.id.writable = False
db.project.created_on.readable = db.project.created_on.writable = False
db.project.created_by.readable = db.project.created_by.writable = False
db.project.modified_by.readable = db.project.modified_by.writable = False
db.project.modified_on.readable = db.project.modified_on.writable = False

db.define_table(
    'task',
    # Field('user_id', 'reference auth_user'),
    Field('title', requires=IS_NOT_EMPTY()),
    Field('description'),
    Field('date', requires=IS_NOT_EMPTY()),
    Field('invited_users'),
    Field('project', 'reference project'),
    auth.signature
)
db.task.id.readable = db.task.id.writable = False
db.task.created_on.readable = db.task.created_on.writable = False
db.task.created_by.readable = db.task.created_by.writable = False
db.task.modified_by.readable = db.task.modified_by.writable = False
db.task.modified_on.readable = db.task.modified_on.writable = False

db.commit()