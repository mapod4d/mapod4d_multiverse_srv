from rest_framework import serializers
from mapod4d.models import Mapod4dVersion


class Mapod4dVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapod4dVersion
        fields = '__all__'


