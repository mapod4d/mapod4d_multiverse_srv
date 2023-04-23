from rest_framework import serializers
from softwares.models import Software



class SoftwareSerializer(serializers.ModelSerializer):
    def get_sversion(self, obj):
        return obj.get_sversion()
 
    sversion = serializers.SerializerMethodField()
 
    class Meta:
        model = Software
        fields = '__all__'

