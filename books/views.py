from django.shortcuts import render
from . import models
from django.views.generic import DetailView

# Create your views here.
class DetailBookView(DetailView):
    model = models.BookModel
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'