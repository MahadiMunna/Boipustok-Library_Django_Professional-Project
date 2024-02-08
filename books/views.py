from django.shortcuts import render, redirect
from . import models
from django.views.generic import DetailView
from . import forms

# Create your views here.
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
        reviewer = self.request.user.account

        borrower = models.BookBorrowerModel.objects.filter(book=post).filter(borrower=reviewer)
        a=1
        if not borrower:
            context['comments'] = comments
            context['comment_form'] = ''
            return context
        else:
            context['comments'] = comments
            context['comment_form'] = comment_form
            return context
            