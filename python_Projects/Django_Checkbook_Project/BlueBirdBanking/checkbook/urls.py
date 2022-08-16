from django.urls import path
from . import views


# Creating necessary URL paths
urlpatterns = [
    # Sets the url path to home page index.html.
    path('', views.home, name='index'),
    # Sets the url path to Create New Account page CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # Sets the url path to Balance Sheet page BalanceSheet.html.
    # Balance Sheet can be displayed using a primary key (<int:pk>
    path('<int:pk>/balance/', views.balance, name='balance'),
    # Sets the url path to Add New Transaction page AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction'),
]
