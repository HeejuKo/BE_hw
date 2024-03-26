"""
URL configuration for wordCount_Prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wordCountApp import views # urls.py에서 wordCountApp의 views.py를 사용 (why? 그 안의 index.html을 찾을 거니까)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name="index"), # 최상단 경로에 유저가 접속하면 views.py에 있는 index 함수 실행
    path('wordCount/', views.wordCount, name="wordCount"),
    path('result/', views.result, name="result"),
    path('hello/', views.hello, name="hello"),
]
