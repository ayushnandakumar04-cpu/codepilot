from django.urls import path
from evaluation.views import SubmissionStartView,AnswerStartView
urlpatterns=[
    path('assessment/<int:pk>/submit/',SubmissionStartView.as_view()),
    path('assessment/<int:pk>/answer/',AnswerStartView.as_view())
]