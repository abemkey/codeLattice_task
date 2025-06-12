from rest_framework import serializers

from My_App.models import Person, User


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'email','phone','age']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'