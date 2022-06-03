from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..Serializer.CourseSerializer import CourseSerializer
from ..Models.Courses import Courses

@api_view(['GET'])
def ShowAll(request):
    courses = Courses.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateCourse(request):
    serializer = CourseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteCourse(request, pk):
    course = Courses.objects.get(courseid=pk)
    course.delete()
    return Response('Items Deleted Successfully')

@api_view(['POST'])
def UpdateCourse(request, pk):
    course = Courses.objects.get(courseid=pk)
    serializer = CourseSerializer(instance=course, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

