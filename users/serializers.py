from rest_framework import serializers
from django.contrib.auth import get_user_model

user = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "profile_pic",
            "role",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        User = user(**validated_data)
        if password:
            User.set_password(password)
        User.save()
        return User
