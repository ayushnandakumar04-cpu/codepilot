from django.urls import path
from accounts.views import AdminCreateView,StudentListCreateView
urlpatterns=[
    path('admin/register/',AdminCreateView.as_view()),
    path('student/register/',StudentListCreateView.as_view())
]