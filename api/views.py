from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, AdminSerializer,TurfDetailsSerializer,TurfImageSerializer
from .models import Admin,turfDetails,turfImages
from rest_framework import viewsets
from django.contrib.auth.models import User



class UserListViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #http_method_names = ['get', 'post']


class AdminListViewset(viewsets.ModelViewSet):
    queryset = Admin.objects.all()  # filter(id=self.request.user.id)
    serializer_class = AdminSerializer   
    #permission_classes = [IsAuthenticated]
    #http_method_names = ['get', 'post']

class TurfDetailsViewset(viewsets.ModelViewSet):
    queryset = turfDetails.objects.all()
    serializer_class = TurfDetailsSerializer

class TurfImageViewset(viewsets.ModelViewSet):
    queryset = turfImages.objects.all()
    serializer_class = TurfImageSerializer