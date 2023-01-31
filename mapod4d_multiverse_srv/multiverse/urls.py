from django.urls import path, include

urlpatterns = [
    path('api/multiverse/', include('multiverse.api.urls')),
]

