from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  #able to allow other domain access /api methods
from rest_framework.parsers import JSONParser #to parse incoming data into data model
from django.http.response import JsonResponse  

#importing our model & Seralizers
from Employeeapp.models import Department,Employees
from Employeeapp.serializers import DepartmentSerializer,EmployeeSerializer
from.myDb import col

@csrf_exempt
def departmentApiList(request):
    if request.method == 'GET':
        departments = list(col.find())  # Retrieve all departments from MongoDB
        serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=department_data)
        if serializer.is_valid():
            col.insert_one(department_data)  # Insert department into MongoDB
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def departmentApiDetail(request, pk):
    if request.method == 'GET':
        department = col.find_one({"DepartmentId": pk})  # Retrieve department by ID from MongoDB
        if department:
            serializer = DepartmentSerializer(department)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"error": "Department not found"}, status=404)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        result = col.update_one({"DepartmentId": pk}, {"$set": department_data})  # Update department in MongoDB
        if result.modified_count > 0:
            return JsonResponse("Updated Successfully", safe=False)
        else:
            return JsonResponse({"error": "Department not found"}, status=404)
    
    elif request.method == 'DELETE':
        result = col.delete_one({"DepartmentId": pk})  # Delete department from MongoDB
        if result.deleted_count > 0:
            return JsonResponse("Deleted Successfully", safe=False)
        else:
            return JsonResponse({"error": "Department not found"}, status=404)

