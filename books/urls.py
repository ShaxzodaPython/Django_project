from django.urls import path
from books.views import header_page

urlpatterns = [
    path('list/', header_page),
]
