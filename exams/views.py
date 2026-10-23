from django.shortcuts import render
from rest_framework.views import APIView
from exams.models import Assessment
from exams.serializers import AssesmentSerializers
from rest_framework import authentication,permissions
from exams.permissions import OwnerOnly
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
class AssessmentListCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request):
        qs = Assessment.objects.filter(created_by=request.user)

        serializer_instance = AssesmentSerializers(qs, many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):
        serializer= AssesmentSerializers(data=request.data)

        if serializer.is_valid():
            start_time = serializer.validated_data["start_time"]
            duration = serializer.validated_data["duration"]

            end_time = (
                datetime.combine(
                    serializer.validated_data["exam_date"],
                    start_time
                ) + timedelta(minutes=duration)
            ).time()

            serializer.save(
                created_by=request.user,
                end_time=end_time
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    

class AssessmentListRetrieveview(APIView):
     authentication_classes=[authentication.TokenAuthentication]
     permission_classes=[OwnerOnly]

     def get(self,request,pk=None):
        qs=get_object_or_404(Assessment,id=pk)
        serializer_instance=AssesmentSerializers(qs)
        return Response(data=serializer_instance.data)
     
     def put(self,request,pk=None):
         instance=get_object_or_404(Assessment,id=pk)
         form_data=request.data
         serializer_instance=AssesmentSerializers(data=form_data,instance=instance)
         if serializer_instance.is_valid(): 
             serializer_instance.save()
             return Response(serializer_instance.data)
         else:
            return Response(serializer_instance.errors)
          

     def delete(self,request,pk=None):
         instance=get_object_or_404(AssesmentSerializers,id=pk)
         instance.delete()
         return Response({"message": "Expense deleted successfully"})