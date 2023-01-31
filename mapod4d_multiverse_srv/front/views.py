from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mapod4d Multiverse'
        return context

class ApiHelpView(TemplateView):
    template_name = "apihelp.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mapod4d Multiverse API Help'
        list = []
        list.append('api/user/login/')
        list.append('api/user/logout/')
        list.append('api/user/logoutall/')
        list.append('api/user/multiverse/')
        list.append('api/user/multiverse/metaverses/')
        list.append('api/user/multiverse/metaverse/<name>')
        list.append('api/user/projects/')
        list.append('api/user/project/<id>')
        list.append('api/user/softwares/')
        list.append('api/user/software/<name>')
        context['list'] = list

        return context

