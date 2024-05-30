from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post


def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'post/list.html', {'posts': posts}) # templates/blog 안의 list.html

# 함수를 실행하기 전에 사용자가 로그인 상태인지 확인
# 사용자가 로그아웃 상태라면 로그인 URL로 redirect시킴
@login_required

# CRUD
def create(request):
    if request.method == "POST":        # 요청된 method가 POST라면
        title = request.POST.get('title') # title을 가져와서 title 변수에 넣고
        content = request.POST.get('content')

        post = Post.objects.create( # POST 객체를 만듦
            title = title,      # 속성 = 받아온 값
            content = content,
        )

        return redirect('post:list') # list.html로 이동
    return render(request, 'post/create.html') #  templates/post 안의 create.html을 보여줌

def detail(request, id): # 데이터의 id를 매개변수로 받음 (id: 각 데이터에 고유하게 부여된 id)
    post = get_object_or_404(Post, id = id) # (사용자가 요청한 id를 가진) Post 데이터를 데이터베이스에서 찾음
    return render(request, 'post/detail.html', {'post': post}) # rendering해서 post로 보냄

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title') # 사용자가 제출한 update.html의 폼에서 title, content 추출
        post.content = request.POST.get('content')
        post.save() # post 데이터의 변경 사항(제목, 내용)을 데이터베이스에 저장
        return redirect('post:detail', id) # 수정이 완료되면, 사용자를 게시글의 상세(detail) 페이지로 이동시킴
    return render(request, 'post/update.html', {'post': post})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete() # 데이터베이스에서 삭제
    return redirect('post:list') # 삭제가 완료되면, 사용자를 메인 페이지로 이동시킴