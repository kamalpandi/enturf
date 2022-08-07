from django.http import JsonResponse
from django.urls import is_valid_path
from requests import request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import UserSerializer, AdminSerializer,TurfDetailsSerializer,TurfImageSerializer
from .models import Admin,turfDetails,turfImages
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import status
"""
def post(self, request, format=None):
    print(request.data)
    serializer = TurfDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Responce(serialier.data, status=status.HTTP_200_OK)
    else:
        return Responce(serialier.errors, status=status.HTTP_400_BAD_REQUEST)

"""

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
    #permission_classes = [IsAuthenticated]

# def modify_input_for_multiple_files(turfDetails, generalTurfImages):
#     dict = {}
#     dict['turfDetails'] = turfDetails
#     dict['generalTurfImages'] = generalTurfImages
#     return dict


class TurfImageViewset(viewsets.ModelViewSet):
    queryset = turfImages.objects.all()#filter(turfDetails__turfName='pk')
    serializer_class = TurfImageSerializer
    #permission_classes = [IsAuthenticated]



    # def get(self, request):
    #     all_image =turfImages.objects.all()
    #     serializer = TurfImageSerializer(all_image, many=True)
    #     return JsonResponse(serializer.data, safe= False)

    # def post(self, request, *args, **kwargs):
    #     turfDetails = request.data['turfDetails']

    #     generalTurfImages = dict((request.data).lists()['generalTurfImages'])
    #     flag = 1
    #     arr=[]
    #     for img_name in generalTurfImages:
    #         modified_data = modify_input_for_multiple_files(turfDetails,img_name)

    #         file_serializer =TurfImageSerializer(data=modified_data)
    #         if file_serializer.is_valid():
    #             file_serializer.save()
    #             arr.append(file_serializer.data)
    #         else:
    #             flag = 0
            
    #         if flag == 1:
    #             return Response(arr, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(arr, status=status.HTTP_400_BAD_REQUEST)