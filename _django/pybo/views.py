from django.shortcuts import get_object_or_404, render

from pybo.models import Question


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
