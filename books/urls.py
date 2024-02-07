from django.urls import path
from . import views

urlpatterns = [
    path('book_details/<int:id>/', views.DetailBookView.as_view(), name='details'),
]