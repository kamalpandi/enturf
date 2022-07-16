from rest_framework import serializers
from .models import Admin, User

#create 
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]

        def create(self, validated_data):
            user = super(UserSerializer, self).create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user

#update  
class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]

        def update(self, instance, validated_data):
            instance.username =validated_data('username', instance.username)
            instance.email = validated_data('email', instance.email)
            instance.password = validated_data('password', instance.password)
            instance.save()
            return instance



class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class AdminUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.__all__ = validated_data('__all__', instance.__all__)
        instance.save()
        return instance