from django.urls import path

from pybo import views

urlpatterns = [
    path('', views.index),  # config/urls.py에서 pybo/ URL을 이미 매핑하였으므로 생략
]
