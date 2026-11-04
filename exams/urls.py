from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from exams.views import AssessmentListCreateView,AssessmentListRetrieveview
urlpatterns=[
     path('token/',ObtainAuthToken.as_view()),
     path('assessment/',AssessmentListCreateView.as_view()),
     path('assessment/<int:pk>/',AssessmentListRetrieveview.as_view())
]