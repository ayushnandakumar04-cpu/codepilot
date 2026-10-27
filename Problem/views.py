from django.shortcuts import render
from rest_framework.views import APIView
from Problem.models import Question
from Problem.serializers import QuestionSerializers
from rest_framework.response import Response
from exams.models import Assessment
from rest_framework.generics import DestroyAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework import authentication,permissions
# Create your views here.
class QuestionCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def post(self,request,pk=None):
        qs=Assessment.objects.get(id=pk)
        form_data=request.data
        serializer_instance=QuestionSerializers(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(assessment=qs,created_by=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class QuestionRetrieveUpdateDeleteView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    queryset=Question.objects.all()
    serializer_class=QuestionSerializers
