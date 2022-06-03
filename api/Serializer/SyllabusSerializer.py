from rest_framework import serializers
from ..Models.Syllabus import Syllabus

class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = '__all__'