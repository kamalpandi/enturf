from rest_framework import serializers
from .models import Admin, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

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

class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Admin
        fields = ['user','id','firstName','lastName','mobileNumber','dateOfBirth','gender','address','pincode']
        depth = 1
        
