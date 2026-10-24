from django.shortcuts import render
from rest_framework.views import APIView
from Problem.models import Question
from Problem.serializers import QuestionSerializers
from rest_framework.response import Response
from Problem.permissions import OwnerOnly
from django.shortcuts import get_object_or_404
from rest_framework import authentication,permissions
# Create your views here.
class QuestionListCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        qs=Question.objects.all()
        serializer_instance=QuestionSerializers(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=QuestionSerializers(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(created_by=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class QuestionListRetrieveView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    def get(self,request,pk=None):
        qs=get_object_or_404(Question,id=pk)
        serializer_instance=QuestionSerializers(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        instance=get_object_or_404(Question,id=pk)
        form_data=request.data
        serializer_instance=QuestionSerializers(data=form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):
        instance=get_object_or_404(Question,id=pk)
        instance.delete()
        return Response({"message":"Question deleted successfully"})