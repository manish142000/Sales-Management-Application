from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    #username_field = get_user_model().USERNAME_FIELD

    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']

        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist() 
        except TokenError:
            self.fail('bad token') 
