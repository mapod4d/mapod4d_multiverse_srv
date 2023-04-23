from django.urls import path
from .views import SoftwareListView, SoftwareDetailView

urlpatterns = [
    path('softwares/', SoftwareListView.as_view(), name='softwares'),
    path('software/<str:name>/<str:so>', SoftwareDetailView.as_view(), name='software'),
]
