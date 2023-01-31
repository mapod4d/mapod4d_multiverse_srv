from django.urls import path
from .views import MainView, ApiHelpView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('api/', ApiHelpView.as_view(), name='api-help'),
]
