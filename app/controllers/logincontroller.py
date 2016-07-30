from ststem.core.controller import *
from datetime import datetime
from flask import Flask, request, redirect, render_template, session, flash, url_for
import re
import os,binascii
import googlemaps
import uuid
import hashlib

# key for maps
gmaps = googlemaps.Client(key='')

class logincontroller(Controller):
    def __init__(self, action):
        super(logincontroller, self).__init_(action)
        self.load_model('LoginModel')
        self.db = self._app.db

# controller for login

def loginReg(self):
    return self.load_view('loginRegistrationLanding.htm')
