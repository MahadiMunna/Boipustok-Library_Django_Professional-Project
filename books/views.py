from django.shortcuts import render, redirect
from . import models
from django.views.generic import DetailView, TemplateView
from . import forms
from .models import BookModel, BookCategory

# Create your views here.
def availableBooks(request, category_slug=None):
    data = BookModel.objects.all()
    if category_slug is not None:
        category = BookCategory.objects.get(slug=category_slug)
        data = BookModel.objects.filter(book_category=category)
    categories = BookCategory.objects.all()
    return render(request, 'available_books.html',{'data':data, 'categories':categories})

class DetailBookView(DetailView):
    model = models.BookModel
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        name = self.request.user.account
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = name
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        if self.request.user.is_authenticated:
            reviewer = self.request.user.account
        else:
            reviewer = None

        borrower = models.BookBorrowerModel.objects.filter(book=post).filter(borrower=reviewer)

        if not borrower:
            context['comments'] = comments
            context['comment_form'] = ''
            return context
        else:
            context['comments'] = comments
            context['comment_form'] = comment_form
            return context
            