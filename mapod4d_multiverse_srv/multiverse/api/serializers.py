from rest_framework import serializers
from multiverse.models import Multiverse, Metaverse, MetaverseVersion
#from projects.api.serializers import ProjectSerializer
from projects.models import Project
from mapod4d.models import Mapod4dVersion


class MetaverseMapod4dVersionSerializer(serializers.ModelSerializer):
    def get_sversion(self, obj):
        return obj.get_sversion()

    sversion = serializers.SerializerMethodField()

    class Meta:
        model = Mapod4dVersion
        fields = ['v1', 'v2', 'v3', 'v4', 'sversion']

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


class MetaverseVersionSerializer(serializers.ModelSerializer):
    fmver_info = MetaverseMapod4dVersionSerializer(source='fmver')
    tmver_info = MetaverseMapod4dVersionSerializer(source='tmver')

    def get_sversion(self, obj):
        return obj.get_sversion()

    sversion = serializers.SerializerMethodField()

    class Meta:
        model = MetaverseVersion
        fields = '__all__'


class MetaverseSerializer(serializers.ModelSerializer):
    project_info = ProjectMetaverseSerializer(source='project')
    metaverseversions = MetaverseVersionSerializer(many=True)
    class Meta:
        model = Metaverse
        fields = '__all__'
        #fields = ['id', 'project_info',]

