from django.urls import path
from .views import list, create, detail, update, delete

app_name = 'blog'
urlpatterns = [
    path('', list, name='list'),
    path('create/', create, name="create"),
    path('detail/<int:id>/', detail, name="detail"), # 몇 번 글을 볼 건지
    path('update/<int:id>/', update, name="update"), # 몇 번 글을 update할 건지
    path('delete/<int:id>', delete, name="delete"), # 몇 번 글을 삭제할 건지
]
