from django.urls import path
from .views import *

# urls.py
app_name = 'contacts'

urlpatterns = [
    path('', IndexView.as_view(), name = "list"),
    #path('result/', search, name = "search"),
    path('create/', create, name="create"),
    path('detail/<int:id>/', detail, name="detail"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]