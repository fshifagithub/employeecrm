from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers import  EmployeeSerializer
from api.models import Employee

# Create your views here.

class EmployeeModelViewSetView(viewsets.ModelViewSet):
    serializer_class=EmployeeSerializer
    model=Employee
    queryset=Employee.objects.all()
    #  localhost:8000/api/v2/employees/department/
    def list(self,request,*args,**Kwargs):
        qs=Employee.objects.all()
        if "department" in request.query_params:
            value=request.query_params.get("department")
            qs=qs.filter(department=value)
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    
    @action(methods=["get"],detail=False)
    def department(self,request,*args,**kwargs):
        qs=Employee.objects.all().values_list("department",flat=True).distinct()
        return Response(data=qs)