from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import loader, RequestContext
from django.http import Http404

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
    # template = loader.get_template('polls/index.html')

    # Template인스턴스의 render()함수를 실행, 인수로 context와 request를 전달
    # 결과로 렌더링 된 HTML문자열이 리턴됨
    # html = template.render(context, request)

    # return HttpResponse(html)
    # 문자열로 표현할때 쉼표로 구분한다
    # latest_question_list의 각 Question의 question_text들을 ', '로 연결시킨
    # 문자열을 output변수에 할당
    # output = ', '.join([q.question_text for q in latest_question_list])
    # 만들어진 질문 제목들을 모은 문자열을 HttpResponse클래스의 생성자로 전달, 인스턴스를 리턴한다.
    return render(request, 'polls/index.html', context)

# def custom_get_object_or_404(model, **kwargs):
#     try:
#         return model.objects.get(**kwargs)
#     except model.objects.get(**kwargs)

    # 1번째 인자로 특정 Model class를 받음
    # 최소 1개 이상의 키워드 인자를 받아서, 받은 인자들을 사용해 주어진
    # Model Class의 get()매서드를 실행
    # 존재하면 해당 인스턴스를 리턴
    # 없으면 raise Http404를 실행 (메시지는 임의로 지정)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, id=question_id)
    context ={
        'question': question,
    }
    return render(request, 'polls/detail.html', context)
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
