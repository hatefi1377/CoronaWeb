from django.urls import path
from . import views
from .views import CaseCreateView , CaseDetailView , CaseUpdateView , CaseDeleteView


urlpatterns = [
    path('', views.home , name = 'home'),
    path('case/<int:pk>/', CaseDetailView.as_view() , name = 'case-detail'),
    path('case/<int:pk>/update/', CaseUpdateView.as_view() , name = 'case-update'),
    path('case/<int:pk>/delete/', CaseDeleteView.as_view() , name = 'case-delete'),
    path('case/new', CaseCreateView.as_view() , name = 'create-case')
]
