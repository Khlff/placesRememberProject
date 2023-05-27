from allauth.account.views import LoginView, LogoutView
from django.urls import path, include

from feedbacker import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('new_feedback/', views.create_feedback, name='create_feedback'),
    path('',views.home, name = 'home')
]
