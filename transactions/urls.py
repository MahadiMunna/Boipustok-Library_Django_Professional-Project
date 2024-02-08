from django.urls import path
from .views import deposit, borrow_books,return_books


# app_name = 'transactions'
urlpatterns = [
    path("deposit/", deposit, name="deposit"),
    path('borrow_now/<int:id>/', borrow_books, name='borrow'),
    path('return/<int:id>/', return_books, name='return'),
]