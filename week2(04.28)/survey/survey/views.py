from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from survey.models import Survey, Answer


def home(request):
    # filter 조건절에 해당
    # [0] 레코드중에서 첫번째 요청
    # select * from survey_survey where status='y' => row 10
    # 최신 데이터 1개만 추출 / 내림차순 : order by('-xx')[index]
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]

    return render(request, "survey/list.html", {'survey': survey})


@csrf_protect
def save_survey(request):
    # 문제 번호와 응답번호를 Answer 객체에 저장한다.
    survey_idx = request.POST["survey_idx"]
    # survey_survey primary key -> 1:n 질문에 대한 답변의 값(survey)
    # ans :선택한 설문의 내용
    dto = Answer(survey_idx=int(request.POST["survey_idx"]), ans=request.POST["num"])
    # insert query 가 호출
    dto.save()
    return render(request, "survey/success.html")


@csrf_protect
def show_result(request, question_id):
    result = Answer.objects.filter(survey_idx=question_id)
    return render(request, "survey/result.html", {'result': result})
