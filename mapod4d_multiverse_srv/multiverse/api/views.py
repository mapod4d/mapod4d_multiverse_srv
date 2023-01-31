from multiverse.models import Metaverse
from multiverse.data import MultiverseData
from .serializers import MetaverseSerializer, MultiverseSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class MultiverseView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = MultiverseData()
        serializer = MultiverseSerializer(data)
        return Response(serializer.data)


class MetaverseListView(generics.ListAPIView):
    serializer_class = MetaverseSerializer

    def get_queryset(self):
        #return Metaverse.objects.all().prefetch_related('project').filter(project__users__id=3)
        if self.request.user.is_authenticated:
            result = Metaverse.objects.all()
        else:
            result = Metaverse.objects.filter(project__name='public').all()
        return result


class MetaverseDetailView(generics.RetrieveAPIView):
    lookup_field = 'mapod4d_id'
    serializer_class = MetaverseSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            result = Metaverse.objects.all()
        else:
            result = Metaverse.objects.filter(project__name='public').all()
        return result

