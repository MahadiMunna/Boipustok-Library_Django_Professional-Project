from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import BookCategory, BookModel

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

def home(request, category_slug=None):
    data = BookModel.objects.all()
    if category_slug is not None:
        category = BookCategory.objects.get(slug=category_slug)
        data = BookModel.objects.filter(book_category=category)
    categories = BookCategory.objects.all()
    return render(request, 'index.html',{'data':data, 'categories':categories})
    
