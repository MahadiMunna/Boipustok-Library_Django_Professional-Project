from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from books.models import BookCategory, BookModel
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

# Create your views here.
def send_contact_email(name, email, feedback):
        message = render_to_string("contact_mail.html", {
            'name' : name,
            'email' : email,
            'feedback' : feedback,
        })
        send_email = EmailMultiAlternatives('Feedback mail from Boipustok', '', to=["mahadimunna.official@gmail.com"])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

class HomeView(TemplateView):
    template_name = 'index.html'

def home(request, category_slug=None):
    data = BookModel.objects.all()
    if category_slug is not None:
        category = BookCategory.objects.get(slug=category_slug)
        data = BookModel.objects.filter(book_category=category)
    categories = BookCategory.objects.all()
    return render(request, 'index.html',{'data':data, 'categories':categories})
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']
            send_contact_email(name, email, feedback)
            messages.success(request,'Your feedback successfully send to the developer. Thank you for your feedback.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html',{'form':form})