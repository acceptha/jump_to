"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

# from pybo import views  # pybo 앱과 관련된 URL

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("pybo/", views.index),  # pybo/ URL이 요청되면 views.index 호출
    path("pybo/", include("pybo.urls")),  # pybo/로 시작되는 URL은 pybo/urls.py 파일 확인
]
