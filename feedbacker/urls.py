from allauth.account.views import LoginView, LogoutView
from django.urls import path, include

from feedbacker import views

urlpatterns = [
    path('accounts/', include('allauth.urls'))
]
