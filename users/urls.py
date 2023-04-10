from django.urls import path
from .views import CreateUserView, UserDetailView

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
]
