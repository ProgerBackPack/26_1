from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from django.urls import path
from users.views import UserUpdate, UserList, UserCreate, PaymentsList, UserDelete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



app_name = UsersConfig.name


urlpatterns = [
    path('', UserList.as_view(),name='users_list'),
    path('update/<int:pk>', UserUpdate.as_view(), name='user_update'),
    path('create/', UserCreate.as_view(), name='user_create'),
    path('delete/<int:pk>', UserDelete.as_view(),name='user_delete'),
    path('payments/', PaymentsList.as_view(), name='payments_list'),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]