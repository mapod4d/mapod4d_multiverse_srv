from django.urls import path
from .views import MetaverseListView, MetaverseDetailView, MultiverseView, MultiverseListView, LastMetaverseVersionDetailView

urlpatterns = [
    path('multiverse/', MultiverseView.as_view(), name='multiverse'),
    path('multiverses/', MultiverseListView.as_view(), name='multiverses'),
    path('multiverse/metaverses/', MetaverseListView.as_view(), name='metaverses'),
    path('multiverse/metaverse/<str:mapod4d_id>/', MetaverseDetailView.as_view(), name='metaverse'),
    path('multiverse/lastmetaverse/<str:metaverse__mapod4d_id>/<str:mapod4dversion>',
            LastMetaverseVersionDetailView.as_view(), name='lastmetaverseversion'),
]
