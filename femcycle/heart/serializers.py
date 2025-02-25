from rest_framework import serializers
from .models import UserData, Profile

class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = '__all__'



class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'age', 'bio', 'location', 'phone_number', 'profile_pic']