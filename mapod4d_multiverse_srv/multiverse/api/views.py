from multiverse.models import Multiverse, Metaverse, MetaverseVersion
from multiverse.data import MultiverseData
from .serializers import MetaverseSerializer, MultiverseDataSerializer, MetaverseVersionSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from django.db.models import Value, F, CharField
from django.db.models.functions import LPad, Cast, Concat



class MultiverseView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = MultiverseData()
        serializer = MultiverseDataSerializer(data)
        return Response(serializer.data)


class MultiverseListView(generics.ListAPIView):
    queryset = Multiverse.objects.all()
    serializer_class = MultiverseDataSerializer


class MetaverseListView(generics.ListAPIView):
    serializer_class = MetaverseSerializer

    def get_queryset(self):
        #return Metaverse.objects.all().prefetch_related('project').filter(project__users__id=3)
        result = Metaverse.objects.order_by('mapod4d_id')
        if self.request.user.is_authenticated:
            pass
        else:
            result = result.filter(project__name='public').all()
        return result


class MetaverseDetailView(generics.RetrieveAPIView):
    lookup_field = 'mapod4d_id'
    serializer_class = MetaverseSerializer

    def get_queryset(self):
        result = Metaverse.objects.order_by('mapod4d_id')
        if self.request.user.is_authenticated:
            pass
        else:
            result = result.filter(project__name='public')
        return result


class LastMetaverseVersionDetailView(generics.RetrieveAPIView):
    lookup_field = 'metaverse__mapod4d_id'
    serializer_class = MetaverseVersionSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        if 'mapod4dversion' not in self.kwargs:
            raise Http404

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        queryset = queryset.filter(**filter_kwargs)

        # filter version
        queryset = queryset.filter(fsversion__lte=self.kwargs['mapod4dversion'])
        queryset = queryset.filter(tsversion__gte=self.kwargs['mapod4dversion'])

        obj = queryset.last()

        if obj is None:
            raise Http404
        self.check_object_permissions(self.request, obj)

        return obj


    def get_queryset(self):
        result = MetaverseVersion.objects.order_by('v1', 'v2', 'v3', 'v4')
        result = result.annotate(
                fsversion=Concat(
                    LPad(Cast("fmver__v1", output_field=CharField()), 3,Value('0')),
                    LPad(Cast("fmver__v2", output_field=CharField()), 3,Value('0')),
                    LPad(Cast("fmver__v3", output_field=CharField()), 3,Value('0')),
                    LPad(Cast("fmver__v4", output_field=CharField()), 3,Value('0')),
                    output_field=CharField()
        ))
        result = result.annotate(
                tsversion=Concat(
                    LPad(Cast("tmver__v1", output_field=CharField()), 3,Value('0')),
                    LPad(Cast("tmver__v2", output_field=CharField()), 3,Value('0')),
                    LPad(Cast("tmver__v3", output_field=CharField()), 3,Value('0')),
                    LPad(Cast("tmver__v4", output_field=CharField()), 3,Value('0')),
                    output_field=CharField()
        ))

        if self.request.user.is_authenticated:
            pass
        else:
            result = result.filter(metaverse__project__name='public')
        return result
