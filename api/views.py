from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import AdminUpdateSerializer, UserSerializer, AdminSerializer, UserUpdateSerializer
from .models import Admin
from rest_framework import generics, viewsets
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
def api_user(request, *args, **kwargs):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)

        return Response(serializer.data)
    return Response({"invalid": "no good data"}, status=400)


# serach the admin table by ID api_admin
@api_view(['GET', 'POST'])
def api_admin(request, *args, **kwargs):
    instance = Admin.objects.filter().values()
    return Response(instance)


class UserListViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']


class UserUpdateViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    #http_method_names = ['get', 'post', 'head', 'put']

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # instance from serializer only accepts id cannot search using name
        print(params['pk'])
        user = User.objects.filter(id=params['pk'])
        serializer = UserUpdateSerializer(user, many=True)
        return Response(serializer.data)


class AdminListViewset(viewsets.ModelViewSet):
    queryset = Admin.objects.all()  # filter(id=self.request.user.id)
    serializer_class = AdminSerializer
    #permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']

    # def get_queryset(self):
    #     queryset = self.queryset
    #     query_set = queryset.all()  # filter(id=self.request.user.id)
    #     return query_set

class AdminUpdateViewset(viewsets.ModelViewSet):
    queryset = Admin.objects.all()  # filter(id=self.request.user.id)
    serializer_class = AdminSerializer
    #permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        # instance from serializer only accepts id cannot search using name
        print(params['pk'])
        user = Admin.objects.filter(id=params['pk'])
        serializer = AdminUpdateSerializer(user, many=True)
        return Response(serializer.data)