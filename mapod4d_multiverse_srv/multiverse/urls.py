from django.urls import path, include

urlpatterns = [
    path('api/', include('multiverse.api.urls')),
]

