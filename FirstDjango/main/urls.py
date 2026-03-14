from django.urls import path
from django.contrib.auth.views import LogoutView

from main.views import IndexView, CustomLoginView, CustomRegisterView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]

