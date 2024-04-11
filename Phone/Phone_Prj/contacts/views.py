from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact

'''
def list(request):
    contacts = Contact.objects.all().order_by('name')

    return render(request, 'list.html', {'contacts': contacts})
'''

class IndexView(ListView): # IndexView라는 클래스 정의
    #model = Contact # 뷰에서 사용할 모델 지정 (Contact 사용) --> queryset 속성 지정 시 model 속성 무시
    queryset = Contact.objects.all().order_by('name')
    template_name = 'list.html' # 이 뷰에서 사용할 템플릿 파일의 경로 지정
    context_object_name = 'contacts' # 템플릿에서 사용할 객체의 이름을 설정 ('contacts'라는 이름으로 Contact 모델 객체 사용)


def search(request):
    search_text = request.GET['search']
    targets = Contact.objects.filter(name__contains = search_text).order_by('name')

    return render(request, 'search.html', {'search': search_text, 'targets': targets})