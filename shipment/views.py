from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.core.mail import send_mail


from .models import Shipment
from .forms import ShipmentCreateForm, ShipmentUpdateForm


class DashboardView(ListView):
    model = Shipment
    template_name = 'shipment/dashboard.html'
    context_object_name = 'shipments'
    paginate_by = 15

    def get_queryset(self, *args, **kwargs):
        qs = super(DashboardView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-created")
        return qs
    

class CreateShipmentView(CreateView):
    template_name = 'shipment/add_shipment.html'
    form_class = ShipmentCreateForm

    def form_valid(self, form):
        form.save()

        #send email
        try:
            send_mail(
                "Subject here",
                "Here is the message.",
                "from@example.com",
                ["to@example.com"],
                fail_silently=False,
            )
        except:
            pass

        messages.success(self.request, 'Your shipment is added successfully')
        return HttpResponseRedirect(reverse_lazy('shipment:add_shipment'))
    

def update_shipment(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    form = ShipmentUpdateForm(request.POST or None, instance=shipment)
    if form.is_valid():
        form.save()
        messages.success(request, 'Shipment is updated successfully')
        return redirect('shipment:dashboard')
    
    return render(request, 'shipment/update_shipment.html', {'form':form})

def delete_shipment(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    shipment.delete()
    messages.success(request, f'Shipment for {shipment.receiver_name} is deleted successfully')
    return redirect('shipment:dashboard')