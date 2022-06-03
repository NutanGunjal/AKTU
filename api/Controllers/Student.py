from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..Serializer.StudentSerializer import StudentSerializer
from ..Models.Student import Student
from rest_framework import filters

@api_view(['GET'])
def ShowAll(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateStudent(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteStudent(pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response('Items Deleted Successfully')

@api_view(['POST'])
def UpdateStudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getStudentFromCourse(request,coursepk):
        student = Student.objects.get(course=coursepk)
        studentserializer = StudentSerializer(instance=student)
        return Response(studentserializer.data)

@api_view(['GET'])
def getStudentFromSyllabus(request, pk,syllabuspk):
    student = Student.objects.get(id=pk,syllabus=syllabuspk)
    studentserializer = StudentSerializer(instance=student)
    return Response(studentserializer.data)

@api_view(['GET'])
def getStudentFromEnrollment(request, pk):
    student = Student.objects.get(id=pk)
    studentserializer = StudentSerializer(instance=student)
    return Response(studentserializer.data)