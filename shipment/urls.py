from django.urls import path
from . import views

app_name = 'shipment'

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('add_shipment/', views.CreateShipmentView.as_view(), name='add_shipment'),
    path('update_shipment/<pk>/', views.update_shipment, name='update_shipment'),
    path('delete_shipment/<pk>/', views.delete_shipment, name='delete_shipment'),

    # neph side
    path('n_dashboard/', views.NDashboardView.as_view(), name='n_dashboard'),
    path('add_package/', views.NCreateShipmentView.as_view(), name='add_package'),
    path('update_package/<pk>/', views.update_package, name='update_package'),
    path('delete_package/<pk>/', views.delete_package, name='delete_package'),
]
