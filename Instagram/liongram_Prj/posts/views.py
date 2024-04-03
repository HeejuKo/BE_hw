from django.shortcuts import render
from .models import Post
from django.db.models import Q

def list(request):
    posts = Post.objects.all().order_by('-created_at') # post 최신순으로 정렬

    return render(request, 'list.html', {'posts': posts})

def search(request):
    search_data = request.GET['data']
    targets = Post.objects.filter(Q(title__contains = search_data) | Q(content__contains = search_data)).order_by('-created_at')

    return render(request, 'search.html', {'data': search_data, 'targets': targets})