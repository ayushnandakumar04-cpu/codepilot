from django.urls import path
from evaluation.views import SubmissionStartView,AnswerStartView,SubmissionRetrieveView,AnswerUpdateView
urlpatterns=[
    path('assessment/<int:pk>/submit/',SubmissionStartView.as_view()),
    path('submission/<int:pk>/answer/',AnswerStartView.as_view()),
    path('submission/<int:pk>/',SubmissionRetrieveView.as_view()),
    path('submission/<int:pk>/retrieve/',SubmissionRetrieveView.as_view()),
    path('answer/<int:pk>/',AnswerUpdateView.as_view())
]