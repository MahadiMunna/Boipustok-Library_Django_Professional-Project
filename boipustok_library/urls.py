from django.contrib import admin
from django.urls import path, include
from core.views import home
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('category/<slug:category_slug>/',home, name='category'),
    path('',include("core.urls")),
    path('books/',include("books.urls")),
    path('users/',include("users.urls")),
    path('transactions/',include("transactions.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
