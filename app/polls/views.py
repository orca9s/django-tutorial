from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    # DB에 있는 Question중, 가장 최근에 발행(pub_date)된 순서대로 최대
    # 5개에 해당하는 QuerySet을  latest_question_list변수에 할당한다.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    # Django의 TEMPLATES설정에 정의된 방법으로,
    # 주어진 인자('polls/index.html')에 해당하는 템플릿 파일을 가지는 Template인스턴스를 생성, 리턴
    template = loader.get_template('polls/index.html')

    # Template인스턴스의 render()함수를 실행, 인수로 context와 request를 전달
    # 결과로 렌더링 된 HTML문자열이 리턴됨
    html = template.render(context, request)
    
    return HttpResponse(html)
    # 문자열로 표현할때 쉼표로 구분한다
    # latest_question_list의 각 Question의 question_text들을 ', '로 연결시킨
    # 문자열을 output변수에 할당
    # output = ', '.join([q.question_text for q in latest_question_list])
    # 만들어진 질문 제목들을 모은 문자열을 HttpResponse클래스의 생성자로 전달, 인스턴스를 리턴한다.
    # return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)