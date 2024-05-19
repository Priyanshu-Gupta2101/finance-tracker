

from django.urls import path
from . import views

urlpatterns = [
    path('income/', views.income_list, name='income_list'),
    path('income/add/', views.income_add, name='income_add'),
    path('income/edit/<int:income_id>/', views.income_edit, name='income_edit'),
    path('income/delete/<int:income_id>/', views.income_delete, name='income_delete'),
    
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add/', views.expense_add, name='expense_add'),
    path('expenses/edit/<int:expense_id>/', views.expense_edit, name='expense_edit'),
    path('expenses/delete/<int:expense_id>/', views.expense_delete, name='expense_delete'),
]
