
from django.contrib.auth.models import User
from django.forms import ValidationError

class CustomAuthentication(object):
    def authenticate(self,request,username,password):
        try:
            user=User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            raise ValidationError("such a user does not exist")
    def get_user(self,id):
        try:
            return User.objects.get(pk=id)
        except:
            return None