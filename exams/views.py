from django.shortcuts import render
from rest_framework.views import APIView
from exams.models import Assessment
from exams.serializers import AssessmentSerializers
from rest_framework import authentication,permissions
from exams.permissions import OwnerOnly
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
# Create your views here.
class AssessmentListCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request):
        qs = Assessment.objects.filter(created_by=request.user)

        serializer_instance = AssessmentSerializers(qs, many=True)

        return Response(data=serializer_instance.data)


         
    def post(self,request):
        form_data=request.data
        serializer = AssessmentSerializers(data=form_data)

        if serializer.is_valid():
            #start_time = serializer.validated_data.get("start_time")
            #duration = serializer.validated_data.get("duration")
            #end_time = (datetime.combine(serializer.validated_data.get("exam_date"),start_time) + timedelta(hours=duration)).time()
            serializer.save(created_by=request.user)
            return Response(serializer.data,status=404)
        return Response(serializer.errors,status=404)
    

class AssessmentListRetrieveview(APIView):
     authentication_classes=[authentication.TokenAuthentication]
     permission_classes=[OwnerOnly]

     def get(self,request,pk=None):
        qs=get_object_or_404(Assessment,id=pk)
        serializer_instance=AssessmentSerializers(qs)
        return Response(data=serializer_instance.data)
     
     def put(self,request,pk=None):
         instance=get_object_or_404(Assessment,id=pk)
         form_data=request.data
         serializer_instance=AssessmentSerializers(data=form_data,instance=instance)
         if serializer_instance.is_valid(): 
             serializer_instance.save()
             return Response(serializer_instance.data)
         else:
            return Response(serializer_instance.errors)
          

     def delete(self,request,pk=None):
         instance=get_object_or_404(Assessment,id=pk)
         instance.delete()
         return Response({"message": "Expense deleted successfully"})