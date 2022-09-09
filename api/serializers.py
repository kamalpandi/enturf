from dataclasses import fields
from rest_framework import serializers
from .models import Admin, BookingReport, CanceledReport, PaymentReport, PlayersAccount, User, turfDetails, turfImages, GroundDetails, GroundImages, GroundPricing, CoachingTime


class GetUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')


# "create_user": "http://127.0.0.1:8000/crud_user/",
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
            # 'id',
            'username',
            'email',
            'password',
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AdminSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.username', read_only=True)
    #user = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = Admin
        fields = ['userName', 'id', 'firstName', 'lastName', 'mobileNumber',
                  'email', 'dateOfBirth', 'gender', 'address', 'pincode', 'user']


class TurfDetailsSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='admin.firstName', read_only=True)

    class Meta:
        model = turfDetails
        # ['images','id','firstName','turfName','mobileNumber','openingTime','cloasingTime','addressOfTurf','aminities','admin',]
        fields = '__all__'


class TurfImageSerializer(serializers.ModelSerializer):
    #generalTurfImages =serializers.ImageField()
    turfName = serializers.CharField(
        source='turfDetails.turfName', read_only=True)
    #turfDetails = serializers.CharField(source='turfDetails.id',read_only=True)

    class Meta:
        model = turfImages
        # ['id','turfDetails','generalTurfImages','turfName']
        fields = '__all__'


class GroundDetailsSerializer(serializers.ModelSerializer):
    turfName = serializers.CharField(
        source='turfDetails.turfName', read_only=True)

    class Meta:
        model = GroundDetails
        fields = '__all__'


class GroundImagesSerializer(serializers.ModelSerializer):
    groundName = serializers.CharField(
        source='GroundDetails.groundName', read_only=True)

    class Meta:
        model = GroundImages
        fields = '__all__'


class GroundPricingSerializer(serializers.ModelSerializer):
    groundName = serializers.CharField(
        source='GroundDetails.groundName', read_only=True)

    class Meta:
        model = GroundPricing
        fields = '__all__'


class CoachingTimeSerializer(serializers.ModelSerializer):
    groundName = serializers.CharField(
        source='GroundDetails.groundName', read_only=True)

    class Meta:
        model = CoachingTime
        fields = '__all__'


class PlayersAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersAccount
        fields = '__all__'


class PaymentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReport
        fields = '__all__'


class BookingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingReport
        fields = '__all__'


class CanceledReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanceledReport
        fields = '__all__'
