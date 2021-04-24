from django.urls import path

from survey import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('save_survey', views.save_survey, name="save"),
    path('show_result/<int:question_id>', views.show_result, name="result"),
]
