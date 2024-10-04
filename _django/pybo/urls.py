from django.urls import path

from pybo import views

app_name = "pybo"

urlpatterns = [
    path("", views.index, name="index"),  # config/urls.py에서 pybo/ URL을 이미 매핑하였으므로 생략
    path("<int:question_id>/", views.detail, name="detail"),
    path("answer/create/<int:question_id>/", views.answer_create, name="answer_create"),
    path("question/create/", views.question_create, name="question_create"),
]
