from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('logout/', views.logout_user, name = 'logout'),
    path('record_details/<int:req_id>/', views.record_details, name = 'record_details'),
    path('add_record/', views.add_record, name = 'add_record'),
    path('delete_record/<int:req_id>/', views.delete_record, name = 'delete_record')
]