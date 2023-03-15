from rest_framework import serializers
from multiverse.models import Metaverse
from multiverse.models import Multiverse
#from projects.api.serializers import ProjectSerializer
from projects.models import Project


class ProjectMetaverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name']


class MultiverseDataSerializer(serializers.Serializer):
    name = serializers.CharField()
    v1 = serializers.IntegerField()
    v2 = serializers.IntegerField()
    v3 = serializers.IntegerField()
    v4 = serializers.IntegerField()


class MultiverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multiverse
        fields = '__all__'


class MetaverseSerializer(serializers.ModelSerializer):
    project_info = ProjectMetaverseSerializer(source='project')
    class Meta:
        model = Metaverse
        fields = '__all__'
        #fields = ['id', 'project_info',]

