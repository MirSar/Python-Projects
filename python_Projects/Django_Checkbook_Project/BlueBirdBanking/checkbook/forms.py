from django.forms import ModelForm
from .models import Account, Transaction


# Creates Account Form based on Account Model
class AccountForm(ModelForm):
    # used to change the behavior of your model fields like
    # changing order options,verbose_name, and a lot of other options
    class Meta:
        model = Account
        fields = '__all__'


# Creates Transaction Form based on Transaction Model
class TransactionForm(ModelForm):
    # used to change the behavior of your model fields like
    # changing order options,verbose_name, and a lot of other options
    class Meta:
        model = Transaction
        fields = '__all__'
