from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication
from evaluation.serializers import SubmissionSerializer
from exams.models import Assessment
from rest_framework.response import Response
from evaluation.permissions import IsStudentUser
from evaluation.models import Submission

# Create your views here.
class SubmissionStartView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStudentUser]
    def post(self,request,pk=None):
        assessment_obj=get_object_or_404(Assessment,id=pk)
        instance=Submission.objects.create(assessment=assessment_obj,student=request.user)
        seializer_instance=SubmissionSerializer(instance)
        return Response(data=seializer_instance.data)

