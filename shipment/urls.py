from django.urls import path
from . import views

app_name = 'shipment'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('add_shipment/', views.CreateShipmentView.as_view(), name='add_shipment'),
    path('update_shipment/<pk>/', views.update_shipment, name='update_shipment'),
    path('delete_shipment/<pk>/', views.delete_shipment, name='delete_shipment'),
]
