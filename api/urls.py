from django.db import router
from django.urls import path, include, re_path
from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserListViewset, AdminListViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('crud_user', UserListViewset, basename='crud_user')
router.register('crud_admin', AdminListViewset, basename='crud_admin')


urlpatterns = [
    path('api_admin/', views.api_admin, name='api_admin'),
    path('api_user/', views.api_user, name='api_user'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path('', include(router.urls))
]
