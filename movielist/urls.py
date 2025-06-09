from django.urls import path
from . import views 

urlpatterns = [
        path('display/', views.display_data, name='display_data'),
        
        path('add/', views.add_data, name='add_data'),
        
        path('', views.display_data, name='home'),
    ]
    