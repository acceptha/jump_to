from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from pybo.form import AnswerForm, QuestionForm
from pybo.models import Answer, Question


def index(request):
    question_list = Question.objects.order_by("-create_date")
    # Question 모델 객체를 이용하여 질문 목록 조회
    # order_by 함수를 사용할 때 컬럼명 앞에 - 기호를 붙이면 역방향 조회를 의미
    context = {"question_list": question_list}
    return render(request, "pybo/question_list.html", context)
    # render 함수는 파이썬 데이터를 HTML로 변환
    # pybo/question_list.html 파일을 생성 후 반환한다는 의미


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)


def answer_create(request, question_id):
    """pybo 답변 등록"""
    question = get_object_or_404(Question, pk=question_id)

    """ 
    답변 생성 방법
    1. Request 데이터의 Form 데이터 중 content 값으로 답변 생성
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    2. Answer 모델을 사용해서 답변 생성
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    """

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("pybo:detail", question_id=question.id)  # 답변 작성 후 질문 상세 페이지를 보여주기 위함
    else:
        # 답변 등록은 POST로만 가능하므로 그 외 메소드는 오류가 발생하도록 작성
        return HttpResponseNotAllowed("Only POST is possible.")
    context = {"question": question, "form": form}
    return render(request, "pybo/question_detail.html", context)


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        # request.POST에 담긴 subject와 content가 인수가 됨
        # QuestionForm 객체는 인수를 받아 form 객체를 생성
        if form.is_valid():
            # POST 폼에 담긴 subject와 content 값이 유효하다면 질문 생성
            question = form.save(commit=False)
            # commit=False는 임시저장
            # form 데이터에는 create_date가 없기 때문에 저장하면 에러 발생
            # create_date 저장하기 위해 question으로 객체를 반환 받음
            question.create_date = timezone.now()
            question.save()
            return redirect("pybo:index")
    else:
        form = QuestionForm()
    context = {"form": form}
    return render(request, "pybo/question_form.html", context)
