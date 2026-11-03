from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from evaluation.serializers import SubmissionSerializer,AnswerSerializer
from exams.models import Assessment
from rest_framework import serializers
from Problem.models import Question
from rest_framework.generics import RetrieveAPIView,UpdateAPIView
from rest_framework.response import Response
from evaluation.permissions import IsStudentUser
from evaluation.models import Submission,Answer
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class SubmissionStartView(APIView):
   # authentication_classes=[authentication.TokenAuthentication]
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsStudentUser]
    def post(self,request,pk=None):
        assessment_obj=get_object_or_404(Assessment,id=pk)
        instance=Submission.objects.create(assessment=assessment_obj,student=request.user)
        seializer_instance=SubmissionSerializer(instance)
        return Response(data=seializer_instance.data)


class AnswerStartView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStudentUser]

    def post(self,request,pk=None):
        submission_obj=get_object_or_404(Submission,id=pk)
        form_data=request.data
        #validation start
        assessment_obj=submission_obj.assessment
        question_obj=Question.objects.filter(assessment=assessment_obj).values_list("id",flat=True)
        question=form_data.get("question")
        if question not in question_obj:
            raise serializers.ValidationError("invalid question, question not exist in assessment")
        #end validation
        serializer_instance=AnswerSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(submission=submission_obj,question=question_obj)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class SubmissionRetrieveView(RetrieveAPIView,UpdateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=SubmissionSerializer

    queryset=Submission.objects.all()

class AnswerUpdateView(APIView):
        
        authentication_classes=[authentication.TokenAuthentication]

        permission_classes=[permissions.IsAdminUser]
    
        def patch(self,request,pk=None):

           print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

           answer_id=pk

           form_data=request.data

           answer_obj=get_object_or_404(Answer,id=answer_id)

           serializer_instance=AnswerSerializer(data=form_data,instance=answer_obj,partial=True)

           serializer_instance.fields["marks_awarded"].read_only=False

           serializer_instance.fields["feedback"].read_only=False

           if serializer_instance.is_valid():

                print(serializer_instance.validated_data,"**************")


                serializer_instance.save()

                return Response(data=serializer_instance.data)
           
           else:

              return Response(data=serializer_instance.errors)