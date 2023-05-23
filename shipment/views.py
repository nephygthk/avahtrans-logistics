from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


from .models import Shipment
from .forms import ShipmentCreateForm, ShipmentUpdateForm

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                pass
                login(request, user)
                return redirect('shipment:dashboard')
            else:
                login(request, user)
                return redirect('shipment:dashboard')
                
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'frontend/login.html')

def send_my_email(subject, message, receiver):
	email = EmailMessage(
		subject,
		message,
		"AvahTrans Delivery <info@avahtrans.com>",
		[receiver],
		)
	email.content_subtype = "html"
	email.fail_silently = False
	email.send()
	return message

class DashboardView(LoginRequiredMixin, ListView):
    model = Shipment
    template_name = 'shipment/dashboard.html'
    context_object_name = 'shipments'
    paginate_by = 15

    def get_queryset(self, *args, **kwargs):
        qs = super(DashboardView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-created")
        return qs
    

class CreateShipmentView(LoginRequiredMixin, CreateView):
    template_name = 'shipment/add_shipment.html'
    form_class = ShipmentCreateForm

    def form_valid(self, form):
        saved_shipment = form.save()

        message = render_to_string('email/shipment_created_email.html',{
        'name': saved_shipment.receiver_name,
        'location': saved_shipment.shipment_location,
        'tracking_code': saved_shipment.tracking_number,
        })

        #send email
        try:
            send_my_email("Shipment location update", message, [saved_shipment.receiver_email])
        except:
            pass

        messages.success(self.request, 'Your shipment is added successfully')
        return HttpResponseRedirect(reverse_lazy('shipment:add_shipment'))
    

@login_required(login_url='shipment:login')
def update_shipment(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    form = ShipmentUpdateForm(request.POST or None, instance=shipment)
    if form.is_valid():
        saved_shipment = form.save()
        message = render_to_string('email/shipment_created_email.html',{
        'name': saved_shipment.receiver_name,
        'location': saved_shipment.shipment_location,
        'tracking_code': saved_shipment.tracking_number,
        })
        print(saved_shipment.receiver_name)
        print(saved_shipment.shipment_location)
        try:
            send_my_email("Shipment dispatch notice", message, [saved_shipment.receiver_email])
        except:
            pass
        finally:
            messages.success(request, 'Shipment is updated successfully')
            return redirect('shipment:dashboard')
    
    return render(request, 'shipment/update_shipment.html', {'form':form})


@login_required(login_url='shipment:login')
def delete_shipment(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    shipment.delete()
    messages.success(request, f'Shipment for {shipment.receiver_name} is deleted successfully')
    return redirect('shipment:dashboard')


@login_required(login_url='shipment:login')
def logoutUser(request):
	logout(request)
	return redirect('shipment:login')