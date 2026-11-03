from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import UserSerializer,StudentProfileSerializer
from accounts.models import User,StudentProfile

from rest_framework import permissions
from evaluation.permissions import IsStudentUser
from rest_framework_simplejwt.authentication  import JWTAuthentication
from rest_framework.response import Response
# Create your views here.
class AdminCreateView(APIView):

    def post(self,request):

        form_data=request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data=serializer_instance.validated_data

            instance=User.objects.create_superuser(role="admin",**cleaned_data)

            serializer_instance=UserSerializer(instance)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class StudentListCreateView(APIView):

    def post(self,request):

        form_data=request.data

        serializer_instance=UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data=serializer_instance.validated_data

            instance=User.objects.create_superuser(role="student",**cleaned_data)

            serializer_instance=UserSerializer(instance)

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class StudentProfileUpdateView(APIView):

    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated,IsStudentUser]

    def put(self,request):

        form_data=request.data

        student_profile=StudentProfile.objects.get(student=request.user)

        serializer_instance=StudentProfileSerializer(instance=student_profile,data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)