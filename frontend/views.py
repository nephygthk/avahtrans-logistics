from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from shipment.models import Shipment

class HomeView(TemplateView):
    template_name = 'frontend/index.html'


class AboutView(TemplateView):
    template_name = 'frontend/about.html'

class ContactView(TemplateView):
    template_name = 'frontend/contact.html'

def TrackingView(request):
    if request.method == 'POST':
        tracking_code = request.POST.get('tracking_code')
        shipments = Shipment.objects.filter(tracking_number=tracking_code)
        if shipments.exists():
            return render(request, 'frontend/tracking.html', {'shipments':shipments}) 
        else:
            messages.error(request, "Invalid tracking code. Please check the code and try again. please make sure no spaces in between the letters")
            return redirect('frontend:home')
    return redirect('frontend:home')
    # return render(request, 'frontend/tracking.html') 