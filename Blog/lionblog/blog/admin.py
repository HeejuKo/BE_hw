from django.contrib import admin
from .models import Post, Category

admin.site.register(Post) # 모델 등록
admin.site.register(Category) # 모델 등록