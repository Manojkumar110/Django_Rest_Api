# from django.shortcuts import render
from rest_framework import viewsets
from api .models import Company,Employee
from api.serielizers import ComapnySerielizer,EmployeeSerielizer
from rest_framework .decorators import action
from rest_framework .response import Response
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = ComapnySerielizer

    @action(detail=True , methods=['get'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(company_id=pk)
            print('COMPANY :-',company)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerielizer(emps , many=True,context = {'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                'massage':'Company Not Exist.'
            })

class EmloyeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerielizer