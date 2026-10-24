from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from exams.views import AssessmentListCreateView,AssessmentListRetrieveview
urlpatterns=[
     path('admin1/token/',ObtainAuthToken.as_view()),
     path('admin1/assessment/',AssessmentListCreateView.as_view()),
     path('admin1/assessment/<int:pk>/',AssessmentListRetrieveview.as_view())
]