from system.core.model import Model
from flask import flash, redirect, session, request
import re
#from datetime import datetime

class LoginModel(Model):
    def __init__(self):
        super(LoginModel, self).__init__()

    def register_user(self,pass_data):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        error=[]
        if not pass_data['email'] or not pass_data['first'] or not pass_data['last'] \
        or not pass_data['password'] or not pass_data['email'] or not pass_data['confirm']:
            flash('cannot have blank fields','blank')

        if not EMAIL_REGEX.match(pass_data['email']):
            flash('email not valid','valid')

        if len(pass_data['password']) < 8:
            flash('password length invalid must be at least 8 chars long','length')

        if (pass_data['password'] != pass_data['password']):
            flash('passwords do not match','match')

        else:
            query="insert into users (first_name, last_name, email, password, hint, created_at, updated_at) values \
            (:first,:last,:email,:password,:hint, now(), now())"
            flash('Successfully created account!  Login to enjoy Message Bored!','success')
            return self.db.query_db(query, pass_data)

