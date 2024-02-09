from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from django.urls import reverse_lazy
from transactions.forms import DepositForm
from django.contrib import messages
from books.models import BookModel, BookBorrowerModel
from datetime import datetime

# Create your views here.
def send_transaction_email(user, email_to, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[email_to])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

def deposit(request):
    deposit_form = DepositForm(request.POST)
    if request.method == 'POST':
        if deposit_form.is_valid():
            amount = deposit_form.cleaned_data.get("amount")
            account = request.user.account
            account.balance += amount
            balance_after_transaction = account.balance
            account.save()
            transaction_instance = Transaction.objects.create(
                account=account,
                amount=amount,
                balance_after_transaction=balance_after_transaction,
                transaction_type="Deposite"
            )
            messages.success(request,f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully')
            send_transaction_email(request.user, request.user.email, amount, "Deposit money Message", "deposit_mail.html")
            return redirect('profile')


    else:
        deposit_form = DepositForm()
    return render(request, 'deposit_form.html', {'form':deposit_form})    

def borrow_books(request, id):
    book = BookModel.objects.get(id=id)
    price = book.price

    borrower = request.user.account

    if borrower.balance<price:
        messages.warning(request, "You don't have enough money for borrow this book. Deposit more money!")
        return render(request, 'profile.html')
    else:
        borrower.balance -= price
        borrower.save()
        transaction_instance = Transaction.objects.create(
            account=borrower,
            amount=price,
            balance_after_transaction=borrower.balance,
            transaction_type="Borrow"
        )
        borrower_model_instance = BookBorrowerModel.objects.create(
            borrower = borrower,
            book = book,
            transaction = transaction_instance
        )
        messages.success(request,f'You have succesfully borrow {book.book_title} for {"{:,.2f}".format(float(price))}$')
        send_transaction_email(request.user, request.user.email, price, "Borrow Book Message", "borrow_mail.html")
        return redirect('profile')

def return_books(request, id):
    bookBorrowerModel = BookBorrowerModel.objects.get(id=id)
    borrower = bookBorrowerModel.borrower
    price = bookBorrowerModel.book.price
    borrower.balance += price
    borrower.save()
    transaction = bookBorrowerModel.transaction
    transaction.transaction_type = "Returned"
    transaction.timestamp = datetime.now()
    transaction.save()
    messages.success(request,f'You have succesfully return \"{bookBorrowerModel.book.book_title}\" and {"{:,.2f}".format(float(price))}$ refunded to your account')
    send_transaction_email(request.user, request.user.email, price, "Return Book Message", "return_mail.html")
    return redirect('profile')