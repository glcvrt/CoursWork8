from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListView, UserCreateView, UserRetrieveView, UserUpdateView, UserDestroyView

app_name = UsersConfig.name


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserListView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='users_create'),
    path('detail/<int:pk>/', UserRetrieveView.as_view(), name='users_detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name='users_delete')
]