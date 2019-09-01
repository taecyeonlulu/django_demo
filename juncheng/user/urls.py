from django.urls import path
from user.views import LoginView,RegisterView

urlpatterns = [
    path(r'user_login/',LoginView.as_view(),name='login')
    # path(r'user_register/',RegisterView.as_view(),name='register')
]

