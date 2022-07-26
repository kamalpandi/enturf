from django.db import router
from django.urls import path, include, re_path
from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserListViewset, AdminListViewset,TurfDetailsViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('create_user', UserListViewset, basename='crud_user')
router.register('create_admin', AdminListViewset, basename='crud_admin')
router.register(r'turf_details',views.TurfDetailsViewset, basename='add_turf_for_admin')
router.register(r'turf_image',views.TurfImageViewset, basename='add_image_for_admin')


urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path('', include(router.urls))
]
