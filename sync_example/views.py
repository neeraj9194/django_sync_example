import pwnedpasswords
# Create your views here.
from passlib.context import CryptContext
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from sync_example.models import UserSecondary

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserSecondary
        fields = ['id', 'username', 'first_name', 'last_name', 'category',
                  'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        if not is_password_secure(password):
            raise ValidationError(detail="The password is unsafe!")
        validated_data["password_hash"] = get_password_hash(password)
        return UserSecondary.objects.create(**validated_data)


class UserViewSet(ModelViewSet):
    queryset = UserSecondary.objects.all()
    serializer_class = UserSerializer


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def is_password_secure(password: str) -> bool:
    """
    accept password, but only if it is safe.
    """
    # Call external API to check password.
    result = pwnedpasswords.check(password)
    if result > 0:
        return False
    return True
