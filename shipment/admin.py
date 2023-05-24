from django.contrib import admin
from .models import Shipment, Package

admin.site.register(Shipment)
admin.site.register(Package)