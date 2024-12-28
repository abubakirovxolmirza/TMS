from django.urls import path
from api.views.auth import RegisterUserView, ListUsersView, UserDetailView, CustomTokenObtainPairView
from api.views.load import LoadListView, LoadDetailView
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('users/', ListUsersView.as_view(), name='list-users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('load/', LoadListView.as_view(), name='load-list'),
    path('load/<int:pk>/', LoadDetailView.as_view(), name='load-detail'),
]
