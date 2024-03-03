from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('<str:slug>', single_page, name='single'),
    path('topic/<str:name>', topic, name='topic'),
    path('contact/', contact_page, name='contact')
]