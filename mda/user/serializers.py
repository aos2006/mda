from rest_framework import serializers, viewsets
from .models import User
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=150, validators=[
        UniqueValidator(
            User.objects.all(),
            'Пользователь с таким email существует',
        )
    ])
    phone = serializers.CharField(max_length=32, validators=[
        UniqueValidator(
            User.objects.all(),
            'Этот номер уже занят'
        )
    ])

    def save(self, data, **kwargs):
        print(data);
        return User.objects.create_user(
            password=data.get('password'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            phone=data.get('phone'),
            username=data.get('first_name') + data.get('email') + data.get('phone')
        )

    class Meta:
        model = User
        fields = (
            'first_name',
            'phone',
            'email',
            'id',
        )


