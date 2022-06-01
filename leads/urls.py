
from django.urls import path
from .views import  (
    LeadCreateView, LeadUpdateView,
    LandingPageView,LeadListView,UpdateView,CreateView,LeadDetailView,
    LeadDeleteView

)
urlpatterns =[
    path('',LeadListView.as_view(),name='lead-list'),
    path('<int:pk>/',LeadDetailView.as_view(),name='lead-detail'),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name='lead-update'),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name='lead-delete'),
    path('create/',LeadCreateView.as_view(),name='lead-create'),
    
] 
app_name='leads'