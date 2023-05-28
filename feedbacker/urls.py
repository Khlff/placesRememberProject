from allauth.socialaccount.providers.vk import views as vk_views
from django.urls import path, include

from feedbacker import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/vk/login/', vk_views.oauth2_login, name='vk_login'),
    path('new_feedback/', views.create_feedback, name='create_feedback'),
    path('home/', views.home, name='home'),
    path('', views.default, name='default')
]
