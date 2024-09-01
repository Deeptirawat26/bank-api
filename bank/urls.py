from django.urls import path
from . import views
from .views import BankListView, BankDetailView, BranchDetailView, BranchListView

urlpatterns = [
    path('', views.index, name='home'),
    path('banks/', BankListView.as_view(), name='bank-list'),
    path('branches/<str:ifsc>/', BranchDetailView.as_view(), name='branch-detail'),  
]
