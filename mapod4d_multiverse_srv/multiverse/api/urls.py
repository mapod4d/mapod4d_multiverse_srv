from django.urls import path
from .views import MetaverseListView, MetaverseDetailView, MultiverseView

urlpatterns = [
    path('', MultiverseView.as_view()),
    path('metaverses/', MetaverseListView.as_view()),
    path('metaverses/<str:mapod4d_id>/', MetaverseDetailView.as_view()),
]
