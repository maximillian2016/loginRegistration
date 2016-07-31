from system.core.controller import *
from datetime import datetime
from flask import Flask, request, redirect, render_template, session, flash, url_for
import re
import os,binascii
#import googlemaps
import uuid
import hashlib

# key for maps
#gmaps = googlemaps.Client(key='')

class logincontroller(Controller):
    def __init__(self, action):
        super(logincontroller, self).__init__(action)
        self.load_model('LoginModel')
        self.db = self._app.db

# controller for login

    def index(self):
        return self.load_view('loginRegistrationLanding.htm')

    def process(self):
        if request.form['action'] == "login":
            print request.form['action']
            return redirect('/')
        else:
            return self.load_view('registration.htm')

    def register_user(self):
        pass_data = {
            'first':request.form['first'], 'last':request.form['last'],'email':request.form['email'],
            'password':request.form['password'], 'hint': request.form['hint']
        }
        print pass_data
        #self.models['LoginModel'].register_user(pass_data)
        return self.load_view('/')

