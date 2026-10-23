from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from exams.views import AssessmentListCreateView,AssessmentListRetrieveview
urlpatterns=[
     path('admin/token/',ObtainAuthToken.as_view()),
     path('admin/assesment/',AssessmentListCreateView.as_view()),
     path('admin/assessment/<int:pk>/',AssessmentListRetrieveview.as_view())
]