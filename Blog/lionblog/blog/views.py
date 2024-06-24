from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment


def list(request):
    # 존재하는 모든 카테고리를 확인할 수 있도록
    categories = Category.objects.all()

    # 선택한 카테고리 id
    category_id = request.GET.get('category') # get 요청으로 온 카테고리 필터링
    
    # 카테고리 필터링
    if category_id: # get 요청으로 들어온 값이 있다면
        category = get_object_or_404(Category, id = category_id)
        posts = category.posts.all().order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/list.html', {'posts': posts, 'categories' : categories}) # templates/blog 안의 list.html

# 함수를 실행하기 전에 사용자가 로그인 상태인지 확인
# 사용자가 로그아웃 상태라면 로그인 URL로 redirect시킴
@login_required

# CRUD
def create(request):
    # 존재하는 모든 카테고리를 확인할 수 있도록 가져옴
    categories = Category.objects.all()

    if request.method == "POST":        # 요청된 method가 POST라면
        title = request.POST.get('title') # title을 가져와서 title 변수에 넣고
        content = request.POST.get('content')
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        category_ids = request.POST.getlist('category') # 선택한 category의 id 리스트 가져옴
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids] # Category 객체로 변환

        post = Post.objects.create( # POST 객체를 만듦
            title = title,      # 속성 = 받아온 값
            content = content,
            author = request.user,
            image = image,
            video = video
        )

        # 다대다 카테고리 연결 (add를 통해)
        for category in category_list:
            post.category.add(category)

        return redirect('blog:list') # list.html로 이동
    return render(request, 'blog/create.html', {'categories' : categories}) # templates/blog 안의 create.html을 보여줌
                                                                            # 글을 생성하면서 존재하는 모든 카테고리를 렌더링할 수 있도록 함

def detail(request, id): # 데이터의 id를 매개변수로 받음 (id: 각 데이터에 고유하게 부여된 id)
    post = get_object_or_404(Post, id = id) # (사용자가 요청한 id를 가진) Post 데이터를 데이터베이스에서 찾음
    return render(request, 'blog/detail.html', {'post': post}) # rendering해서 post로 보냄

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title') # 사용자가 제출한 update.html의 폼에서 title, content 추출
        post.content = request.POST.get('content')
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        # 새로운 파일을 업로드했다면, 이전 파일 삭제 후 새로운 파일로 업데이트
        if video:
            post.video.delete()
            post.video = video
        if image:
            post.image.delete()
            post.image = image

        post.save() # post 데이터의 변경 사항(제목, 내용)을 데이터베이스에 저장
        return redirect('blog:detail', id) # 수정이 완료되면, 사용자를 게시글의 상세(detail) 페이지로 이동시킴
    return render(request, 'blog/update.html', {'post': post})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete() # 데이터베이스에서 삭제
    return redirect('blog:list') # 삭제가 완료되면, 사용자를 메인 페이지로 이동시킴

def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            post = post
        )
        return redirect('blog:detail', post_id)

# 좋아요를 누른 사용자 목록에 request.user 추가
def add_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.like.add(request.user)
    return redirect('blog:detail', post_id)

# 좋아요를 누른 사용자 목록에 request.user 삭제
def remove_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.like.remove(request.user)
    return redirect('blog:detail', post_id)

def mylike(request):
    liked_posts = Post.objects.filter(like = request.user).order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts' : liked_posts}) # myblog.html과 구조가 동일하기 때문에 그냥 myblog 페이지로 연결