from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..Serializer.SyllabusSerializer import SyllabusSerializer
from ..Models.Syllabus import Syllabus

@api_view(['GET'])
def ShowAll(request):
    syllabus = Syllabus.objects.all()
    serializer = SyllabusSerializer(syllabus, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateSyllabus(request):
    serializer = SyllabusSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteSyllabus(request, pk):
    syllabus = Syllabus.objects.get(id=pk)
    syllabus.delete()
    return Response('Items Deleted Successfully')

@api_view(['POST'])
def UpdateSyllabus(request, pk):
    syllabus = Syllabus.objects.get(id=pk)
    serializer = SyllabusSerializer(instance=syllabus, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)