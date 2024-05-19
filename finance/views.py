
from django.shortcuts import render, get_object_or_404, redirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm

# Income Views
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'finance/income_list.html', {'incomes': incomes})

def income_add(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'finance/income_form.html', {'form': form})

def income_edit(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'finance/income_form.html', {'form': form})

def income_delete(request, income_id):
    income = get_object_or_404(Income, id=income_id, user=request.user)
    if request.method == 'POST':
        income.delete()
        return redirect('income_list')
    return render(request, 'finance/income_confirm_delete.html', {'income': income})

# Expense Views
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'finance/expense_list.html', {'expenses': expenses})

def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'finance/expense_form.html', {'form': form})

def expense_edit(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'finance/expense_form.html', {'form': form})

def expense_delete(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'finance/expense_confirm_delete.html', {'expense': expense})
