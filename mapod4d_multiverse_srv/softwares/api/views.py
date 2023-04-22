from softwares.models import Software
from .serializers import SoftwareSerializer
from rest_framework import generics
from django.http import Http404



class SoftwareListView(generics.ListAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer


class SoftwareDetailView(generics.RetrieveAPIView):
    lookup_field='name'
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        queryset = queryset.filter(**filter_kwargs)

        queryset = queryset.order_by('v1', 'v2', 'v3', 'v4')

        obj = queryset.last()

        if obj is None:
            raise Http404
        self.check_object_permissions(self.request, obj)

        return obj

