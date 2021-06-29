# Django 수행

## 스크립트 (순서대로 수행)
만약 python2와 python3가 같이 깔려있다면 python3로 수행



### `python -m venv myvenv`
가상환경을 만들어 줍니다.




### `source ./myvenv/bin/activate`
가상환경을 켜줍시다.(윈도우에서는 명령어가 조금 다를 수 있습니다.)




### `pip install -r requirements.txt`
현재 프로젝트에 필요한 django, django-cors-headers 등을 다운 받아줍니다. \
궁금하시면 requirements.txt 을 한번 보시는 것도 좋습니다. pacakge.json 과 비슷하게 프로젝트내의 사용되는 각각의 라이브러리 명과 버전 정보를 가지고 있습니다. 




### `python manage.py runserver`
서버를 구동시킵니다.
