from django.contrib.auth.models import User
from rest_framework import serializers
class RegistartionSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model=User
        fields=["username","email", "password","password2" ]
        extra_kwargs={"password": {"write_only": True}}
