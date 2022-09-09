# get_object_or_404 is needed to use pk to find account data.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# This function will render the Home page when requested.
def home(request):
    # Passing in the Transaction form
    form = TransactionForm(data=request.POST or None) # Retrieve Transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        # If the form is submitted, retrieve which account the user wants to view
        pk = request.POST['account']
        # Call balance function to render that account's Balance Sheet
        return balance(request, pk)
    # Pass content to the template in a dictionary
    content = {'form': form}
    # Adds content of form to page
    return render(request, 'checkbook/index.html', content)


# This function will render the Create New Account page when requested.
def create_account(request):
    form = AccountForm(data=request.POST or None)  # Retrieves the Account Form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # check to see if the submitted form is valid and if so, saves the form
            form.save()  # Saves new account
            return redirect('index')  # Returns user back to the home page
    content = {'form': form}  # Saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# This function will render the Balance Sheet page when requested.
def balance(request, pk):
    # Retrieve the requested account using its primary key
    account = get_object_or_404(Account, pk=pk)
    # Retrieve all of that account's transactions
    transactions = Transaction.Transactions.filter(account=pk)
    # Create account total variable, starting with initial deposit value
    current_total = account.initial_deposit
    # Create a dictionary into which transaction info will be placed
    table_contents = {}
    # Loop through transactions and determine which is a deposit or withdrawal
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            # Add transaction and total to the dictionary
            table_contents.update({t: current_total})
        else:
            # If withdrawal then subtract amount from balance
            current_total -= t.amount
            # Add transaction and total to the dictionary
            table_contents.update({t: current_total})
    # Pass account, account total balance, and transaction info to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# This function will render the Add Transaction page when requested.
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # Retrieves the Transaction Form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # check to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account']  # Retrieve which account the transaction was for
            form.save()  # Saves the transaction form
            return balance(request, pk)  # Renders balance of the accounts Balance Sheet
    # Pass content to the template in a dictionary
    content = {'form': form}
    # adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
