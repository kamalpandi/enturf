from rest_framework import serializers
from .models import Admin, User, turfDetails
from django.contrib.auth import get_user_model
from drf_writable_nested import WritableNestedModelSerializer



#"create_user": "http://127.0.0.1:8000/crud_user/",
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

#"create_admin": "http://127.0.0.1:8000/crud_admin/", 
class AdminSerializer(serializers.ModelSerializer):
    userName =serializers.CharField(source='user.username',read_only=True)
    #user = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = Admin
        fields = ['userName','id','firstName','lastName','mobileNumber','dateOfBirth','gender','address','pincode','user']

class TurfDetailsSerializer(serializers.ModelSerializer):
    firstName =serializers.CharField(source='admin.firstName',read_only=True)
    generalTurfImages = serializers.ImageField(max_length=None, allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model = turfDetails
        fields = '__all__'
         




# #"list_user_admin": "http://127.0.0.1:8000/list_user_admin/"
# class AdminListSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
#     class Meta:
#         model = Admin
#         fields = ['user','firstName','lastName','mobileNumber','dateOfBirth','gender','address','pincode']

# class UserListSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
#     username = serializers.CharField(read_only=True)
#     email = serializers.CharField(read_only=True)
#     admin = AdminListSerializer()
#     class Meta:
#         model = User
#         fields = [
#             'id',
#             'username',
#             'email',
#             'admin',
#         ]

#use this to exclude the password(also add other fields too) retrived from db #https://www.abheist.com/django-hide-serializer-depth-fields/
# class UserPassSerializer(serializers.ModelSerializer):
#     username =serializers.CharField(read_only=True)
#     class Meta:
#         model = get_user_model()
#         exclude =['password','last_login','first_name','last_name','is_staff','is_active','groups','user_permissions','is_superuser','date_joined','email']
    
# class AdminSerializer(serializers.ModelSerializer):
#     #user = UserPassSerializer()    
#     name = serializers.CharField(source='user.username',read_only=True)
#     uid = serializers.CharField(source='user.id',read_only=True)
#     # 'uid','name','user',
#     class Meta:
#         model = Admin
#         fields = ['uid','name','id','firstName','lastName','mobileNumber','dateOfBirth','gender','address','pincode']
#         depth = 1