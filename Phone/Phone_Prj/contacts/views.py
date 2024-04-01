from django.shortcuts import render
from .models import Contact

def list(request):
    contacts = Contact.objects.all().order_by('name')

    return render(request, 'list.html', {'contacts': contacts})

def search(request):
    search_text = request.GET['search']
    targets = Contact.objects.filter(name__contains = search_text).order_by('name')

    return render(request, 'search.html', {'search': search_text, 'targets': targets})