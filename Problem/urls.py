from django.urls import path
from Problem.views import QuestionListCreateView,QuestionListRetrieveView
urlpatterns=[
    path('question/',QuestionListCreateView.as_view()),
    path('<int:pk>/',QuestionListRetrieveView.as_view())

]