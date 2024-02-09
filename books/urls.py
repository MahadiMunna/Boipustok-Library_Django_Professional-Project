from django.urls import path
from . import views

urlpatterns = [
    path('', views.availableBooks, name='books'),
    path('category/<slug:category_slug>/',views.availableBooks, name='category_book'),
    path('book_details/<int:id>/', views.DetailBookView.as_view(), name='details'),
]