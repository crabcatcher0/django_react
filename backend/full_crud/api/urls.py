from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('books/<int:id>', book_detail, name='book')
]
