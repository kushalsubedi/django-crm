
from django.urls import path
from .views import home_page, lead_create,lead_detail, lead_update

urlpatterns =[
    path('',home_page),
    path('<int:pk>/',lead_detail),
    path('<int:pk>/update/',lead_update),
    path('create/',lead_create),
    
] 