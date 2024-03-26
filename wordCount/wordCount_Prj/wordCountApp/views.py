from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    entered_text = request.GET['fulltext'] # 요청이 들어오면 fulltext를 가져옴
    word_list = entered_text.split() # entered_text를 공백 기준으로 문자열을 나눔

    word_dictionary = {}
    count_num = 0

    for word in word_list:          # {word : 출현 횟수}로 만들어줌
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
        count_num += 1

    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'count': count_num}) # result.html 가져가서 사용할 변수 챙김