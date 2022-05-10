
from django.urls import path
from .views import home_page, lead_create,lead_detail, lead_update,lead_delete

urlpatterns =[
    path('',home_page,name='lead-list'),
    path('<int:pk>/',lead_detail,name='lead-detail'),
    path('<int:pk>/update/',lead_update,name='lead-update'),
    path('<int:pk>/delete/',lead_delete,name='lead-delete'),
    path('create/',lead_create,name='lead-create'),
    
] 
app_name='leads'