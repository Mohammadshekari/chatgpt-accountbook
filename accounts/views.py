from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm

def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})

def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = account.transaction_set.all()
    return render(request, 'accounts/account_detail.html', {'account': account, 'transactions': transactions})

def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'accounts/account_form.html', {'form': form})

def add_transaction(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.account = account
            transaction.save()
            return redirect('account_detail', pk=pk)
    else:
        form = TransactionForm()
    return render(request, 'accounts/transaction_form.html', {'form': form, 'account': account})
