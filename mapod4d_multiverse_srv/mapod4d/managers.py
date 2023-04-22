from django.db import models
from django.db.models import Value, F, CharField
from django.db.models.functions import LPad, Cast, Concat


class Mapod4dVersionManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().annotate(
                    sversion=Concat(
                        LPad(Cast("v1", output_field=CharField()), 3,Value('0')),
                        LPad(Cast("v2", output_field=CharField()), 3,Value('0')),
                        LPad(Cast("v3", output_field=CharField()), 3,Value('0')),
                        LPad(Cast("v4", output_field=CharField()), 3,Value('0')),
                        output_field=CharField()
                    ))
         #filter(sversion__lt="001002003004")

#    def get_queryset_filtered_by_version(self)
#        return get_queryset().filter(sversion__lt="001002003004")

