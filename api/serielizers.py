from rest_framework import serializers
from api .models import Company,Employee

# Create serializer Here

class ComapnySerielizer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerielizer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'