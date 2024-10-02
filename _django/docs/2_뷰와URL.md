# 2장 장고의 기본 요소 익히기!

## App

```shell
django-admin startapp pybo
```

- `startapp` 명령어를 이용하여 pybo 앱 생성
- 현재 디렉토리 하위에 `pybo` 앱 디렉토리가 생성됨
- `config/urls.py`과 `pybo/view.py` 파일로 라우팅 관리

<pre>
_django/
 └─ pybo/
     ├─ migrations/
     │   └─ __init__.py
     ├─ __init__.py
     ├─ admin.py
     ├─ apps.py
     ├─ models.py
     ├─ tests.py
     └─ views.py
</pre>

- `pybo/views.py`
    - Response 함수 작성


### 장고 개발 흐름

![기본 흐름](https://wikidocs.net/images/page/70649/2-01_6.png)

1. 브라우저에서 로컬 서버로 http://localhost:8000/pybo 페이지 요청
2. `urls.py` 파일에서 `/pybo` URL 매핑을 확인 후 `views.py` 파일의 `index` 함수 호출
3. 호출한 결과를 브라우저에 반영

## URL 분리

- `pybo` 앱에 관련된 내용은 해당 디렉토리 하위에 위치해야 관리하기 편함
- `pybo` 앱에서만 사용되는 URL은 `config/urls.py` 위치가 아닌 `pybo/urls.py` 파일에서 관리
- `config/urls.py`의 URL과 include 함수로 매핑된 URL을 합쳐서 라우팅

| config/urls.py | +   | pybo/urls.py       | =   | 최종 URL                  |
|----------------|-----|--------------------|-----|-------------------------|
| 'pybo/'        | +   | ''                 | =   | 'pybo/'                 |
| 'pybo/'        | +   | 'question/create/' | =   | 'pybo/question/create/' |
