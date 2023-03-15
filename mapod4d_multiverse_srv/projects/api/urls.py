from django.urls import path
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('projects', ProjectListView.as_view(), name='projects'),
    path('project/<str:pk>/', ProjectDetailView.as_view(), name='project'),
]
