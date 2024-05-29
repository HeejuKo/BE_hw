from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', list, name='list'),
    path('create/', create, name="create"),
    path('detail/<int:id>/', detail, name="detail"), # 몇 번 글을 볼 건지
    path('update/<int:id>/', update, name="update"), # 몇 번 글을 update할 건지
    path('delete/<int:id>', delete, name="delete"), # 몇 번 글을 삭제할 건지
    path('create-comment/<int:post_id>/', create_comment, name="create-comment"),
    # 다대다 좋아요
    path('add-like/<int:post_id>/', add_like, name="add-like"),
    path('remove-like/<int:post_id>/', remove_like, name="remove-like"),
    path('my-like/', mylike, name="my-like")
]
