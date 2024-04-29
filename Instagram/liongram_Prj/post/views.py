from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.db.models import Q

def list(request):
    posts = Post.objects.all().order_by('-created_at') # post 최신순으로 정렬

    return render(request, 'post/list.html', {'posts': posts})

def search(request):
    search_data = request.GET['data']
    targets = Post.objects.filter(Q(title__contains = search_data) | Q(content__contains = search_data)).order_by('-created_at')

    return render(request, 'post/search.html', {'data': search_data, 'targets': targets})

# CRUD
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title = title,
            content = content,
        )

        return redirect('list')
    return render(request, 'post/create.html')

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    post.views += 1
    post.save()
    return render(request, 'post/detail.html', {'post': post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('detail', id)
    return render(request, 'post/update.html', {'post': post})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('list')