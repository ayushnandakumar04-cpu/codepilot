from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication
from evaluation.serializers import SubmissionSerializer,AnswerSerializer
from exams.models import Assessment
from Problem.models import Question
from rest_framework.response import Response
from evaluation.permissions import IsStudentUser
from evaluation.models import Submission,Answer

# Create your views here.
class SubmissionStartView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStudentUser]
    def post(self,request,pk=None):
        assessment_obj=get_object_or_404(Assessment,id=pk)
        instance=Submission.objects.create(assessment=assessment_obj,student=request.user)
        seializer_instance=SubmissionSerializer(instance)
        return Response(data=seializer_instance.data)


class AnswerStartView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStudentUser]


    def post(self, request, pk=None):

            qs = Assessment.objects.get(id=pk)

            submission_obj = Submission.objects.get(
                assessment=qs,
                student=request.user
            )

            question_obj = Question.objects.get(
                id=request.data.get('question'),
                assessment=qs
            )

            form_data = request.data

            serializer_instance = AnswerSerializer(data=form_data)

            if serializer_instance.is_valid():

                serializer_instance.save(
                    submission=submission_obj,
                    question=question_obj
                )

                return Response(serializer_instance.data)

            else:
                return Response(serializer_instance.errors)

            
