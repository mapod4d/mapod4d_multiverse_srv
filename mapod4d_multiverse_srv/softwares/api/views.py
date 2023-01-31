from softwares.models import Software
from .serializers import SoftwareSerializer
from rest_framework import generics



class SoftwareListView(generics.ListAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer


class SoftwareDetailView(generics.RetrieveAPIView):
    lookup_field='name'
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer

