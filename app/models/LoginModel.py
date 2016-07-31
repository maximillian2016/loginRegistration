from system.core.model import Model
import re
from datetime import datetime

class LoginModel(Model):
    def __inint__(self):
        super(LoginModel, self).__init__()

    def register_user(self):
        query="insert into users (first_name, last_name, email, password, hint, created_at, updated_at) values\
        (':first', ':last', ':email', ':password', ':hint', now(), now())"


