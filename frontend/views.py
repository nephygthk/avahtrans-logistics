from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'frontend/index.html'


class AboutView(TemplateView):
    template_name = 'frontend/about.html'

class ContactView(TemplateView):
    template_name = 'frontend/contact.html'

def TrackingView(request):
    if request.method == 'POST':
        pass
    return render(request, 'frontend/tracking.html', {}) 