from django.urls import path
from .views import add_user, get_users, receive_survey, home

urlpatterns = [
    path('', home),
    path('add_user/', add_user),
    path('users/', get_users),
    path('api/survey/', receive_survey),
]
