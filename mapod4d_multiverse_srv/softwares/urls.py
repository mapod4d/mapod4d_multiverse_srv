from django.urls import path, include

urlpatterns = [
    path('api/', include('softwares.api.urls')),
]

