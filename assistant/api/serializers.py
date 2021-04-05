from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from assistant.db.people import get_people_by_auth_id


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            refresh = self.get_token(self.user)
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            data['username'] = self.user.username
            auth_user_ref = get_people_by_auth_id(self.user.id)
            data['org_id'] = auth_user_ref.org_id
            data['auth_id'] = self.user.id
            data['type'] = auth_user_ref.type
            return data
        except:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
