from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        data = {
            'bolimlar': Bolim.objects.all()[:8]
        }
        return render(request, 'page-index-2.html', data)

class BolimlarView(View):
    def get(self, request):
        data = {
            'bolimlar': Bolim.objects.all()
        }
        return render(request, 'page-category.html', data)

class IchkiView(View):
    def get(self, request, pk):
        data = {
            'ichkilar': Bolim.objects.get(id=pk).bolim_ichkilari.all()
        }
        return render(request, 'ichki.html', data)

class AsosiyView(View):
    def get(self, request):
        data = {
            'bolimlar': Bolim.objects.all()[:8]
        }
        return render(request, 'page-index.html', data)

class Page_listView(View):
    def get(self, request):
        data = {
            'ichkisi': Bolim.objects.all()
        }
        return render(request, 'page-listing-grid.html', data)