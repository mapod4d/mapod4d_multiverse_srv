from django.urls import path
from .views import MetaverseListView, MetaverseDetailView, MultiverseView

urlpatterns = [
    path('', MultiverseView.as_view(), name='multiverse'),
    path('metaverses/', MetaverseListView.as_view(), name='metaverses'),
    path('metaverse/<str:mapod4d_id>/', MetaverseDetailView.as_view(), name='metaverse'),
]
