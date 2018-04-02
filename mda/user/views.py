from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        model = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'phone': request.data.get('phone'),
            'first_name': request.data.get('name')
        }

        serializer = UserSerializer(
            data=model,
            context={'request': request}
        )

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.save(serializer.data)

        return Response(serializer.data, status=201)
