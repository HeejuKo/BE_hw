from django.urls import path
from .views import *

# urls.py
app_name = 'contacts'

urlpatterns = [
    path('', IndexView.as_view(), name = "list"),
    path('result/', search, name = "search"),
]