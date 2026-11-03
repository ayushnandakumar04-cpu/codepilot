from django.urls import path
from accounts.views import AdminCreateView,StudentListCreateView,StudentProfileUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns=[
    path('admin/register/',AdminCreateView.as_view()),
    path('student/register/',StudentListCreateView.as_view()),
    path('jwt/token/',TokenObtainPairView.as_view()),
    path('jwt/token/refresh/',TokenRefreshView.as_view()),
    path('profile/update/',StudentProfileUpdateView.as_view())
]