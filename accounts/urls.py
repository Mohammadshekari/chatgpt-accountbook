from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_list, name='account_list'),
    path('account/<int:pk>/', views.account_detail, name='account_detail'),
    path('account/new/', views.add_account, name='add_account'),
    path('account/<int:pk>/transaction/new/', views.add_transaction, name='add_transaction'),
]
