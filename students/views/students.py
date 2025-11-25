from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from students.models import Students
from students.serializer import StudentsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
   queryset = Students.objects.all()
   serializer_class = StudentsSerializer