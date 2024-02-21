from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import *
from .serializers import *

# class StudentAPI(APIView):
#     def get(self, request):
#         student_obj = Student.objects.all()
#         serializers = StudentSerializer(student_obj, many=True)
#         return render(request, 'index.html', {'student': serializers.data})
#         # return Response({'status': 200, 'payload': serializers.data})

#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)

#         if not serializer.is_valid():
#             print(serializer.errors)
#             return HttpResponse('something went wrong')
#             # return Response({'status':403, 'errors':serializer.errors , 'massage':'something went wrong!'})
    
#         serializer.save() # to save the data
#         return redirect('student')
        # return Response({'status':200, 'payload': serializer.data ,'massage': 'Data inserted successfully!'})

# class StudentAPI_up_or_del(APIView):
#     def patch(self, request):
#         try:
#             student_obj = Student.objects.get(id = request.data['id'])
#             serializer = StudentSerializer(student_obj, data=request.data, partial=True)
#                                                                     #partial true means it canbe update partially

#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({'status':403, 'errors':serializer.errors , 'massage':'something went wrong!'})
                
#             serializer.save()
#             return Response({'status':200, 'payload': serializer.data ,'massage': 'Data inserted successfully!'})
#         except Exception as e:
#             print(e)
#             return Response({'status':404, 'massage': 'id not found'})

#         # def patch(self, request):
#         #     pass

#     def delete(self, request):
#         try:
#             id = request.GET.get('id')  # we also can get id like query
#             student_obj = Student.objects.get(id =id)
#             student_obj.delete()
#             return Response({'status':201, 'massage': 'Data deleted successfully!'})
#         except Exception as e:
#             print(e)
#             return Response({'status':404, 'massage': 'id not found'})  



@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    serializers = StudentSerializer(student_obj, many=True)
    return render(request, 'index.html', {'student': serializers.data})
    # return Response({'status': 200, 'payload': serializers.data})


@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403, 'errors':serializer.errors , 'massage':'something went wrong!'})
    
    serializer.save()
    return Response({'status':200, 'payload': serializer.data ,'massage': 'Data inserted successfully!'})

@api_view(['PUT', 'PATCH'])  # Put method called full pacaket it cannot update data partially
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id = id)
        serializer = StudentSerializer(student_obj, data=request.data, partial=True)
                                                             #partial true means it can be update partially

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'errors':serializer.errors , 'massage':'something went wrong!'})
        
        serializer.save()
        return Response({'status':200, 'update': serializer.data ,'massage': 'Data inserted successfully!'})
    except Exception as e:
        print(e)
        return Response({'status':404, 'massage': 'id not found'})
    

@api_view(['DELETE'])
def delete_student(request):
    try:
        id = request.GET.get('id')  # we also can get id like query
        student_obj = Student.objects.filter(id = id)
        student_obj.delete()
        return Response({'status':201, 'massage': 'Data deleted successfully!'})
    except Exception as e:
        print(e)
        return Response({'status':404, 'massage': 'id not found'})