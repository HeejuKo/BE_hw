from django.urls import path
from .views import list, detail, update

app_name = 'post'
urlpatterns = [
    path('', list, name='list'),
    path('detail/<int:id>/', detail, name="detail"), # 몇 번 글을 볼 건지
    path('update/<int:id>/', update, name="update"), # 몇 번 글을 update할 건지
]