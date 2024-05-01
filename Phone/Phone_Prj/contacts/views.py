from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Contact

'''
def list(request):
    contacts = Contact.objects.all().order_by('name')

    return render(request, 'contacts/list.html', {'contacts': contacts})
'''

class IndexView(ListView): # IndexView라는 클래스 정의
    #model = Contact # 뷰에서 사용할 모델 지정 (Contact 사용) --> queryset 속성 지정 시 model 속성 무시
    queryset = Contact.objects.all().order_by('name')
    template_name = 'contacts/list.html' # 이 뷰에서 사용할 템플릿 파일의 경로 지정
    context_object_name = 'contacts' # 템플릿에서 사용할 객체의 이름을 설정 ('contacts'라는 이름으로 Contact 모델 객체 사용)

'''
def search(request):
    search_text = request.GET['search']
    targets = Contact.objects.filter(name__contains = search_text).order_by('name')

    return render(request, 'contacts/search.html', {'search': search_text, 'targets': targets})
'''

# CRUD
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        contact = Contact.objects.create(
            name = name,
            phone_num = phone_num,
            email = email,
        )

        return redirect('contacts:list')
    return render(request, 'contacts/create.html')

def detail(request, id):
    contact = get_object_or_404(Contact, id = id)
    return render(request, 'contacts/detail.html', {'contact': contact})

def update(request, id):
    contact = get_object_or_404(Contact, id = id)
    if request.method == "POST":
        contact.name = request.POST.get('name')
        contact.phone_num = request.POST.get('phone_num')
        contact.email = request.POST.get('email')
        contact.save()
        return redirect('contacts:detail', id)
    return render(request, 'contacts/update.html', {'contact': contact})

def delete(request, id):
    contact = get_object_or_404(Contact, id = id)
    if request.method == "POST":
        contact.delete()
        return redirect('contacts:list')
    return render(request, 'contacts/delete.html', {'contact': contact})