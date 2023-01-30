from django.urls import path, include

urlpatterns = [
    path('', include('multiverse.api.urls')),
]

