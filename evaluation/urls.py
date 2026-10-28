from django.urls import path
from evaluation.views import SubmissionStartView
urlpatterns=[
    path('assessment/<int:pk>/submit/',SubmissionStartView.as_view())
]