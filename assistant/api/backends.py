from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            print("[CustomBackend]start")
            user = User.objects.get(Q(username=username))
            if user.check_password(password):
                return user
        except Exception:
            return None
