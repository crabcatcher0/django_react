from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def homepage(request):
    book_list = Book.objects.all()
    serializer = BookSerializer(book_list, many=True)
    serialized_data = serializer.data
    
    if request.method == 'POST':
        add_book = BookSerializer(data=request.data)
        if add_book.is_valid():
            add_book.save()
            return Response(add_book.data, status=status.HTTP_201_CREATED)
        
    return Response(serialized_data)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, id):
    book_data = get_object_or_404(Book, id=id)
    
    if request.method == 'PUT':
        edit_book = BookSerializer(book_data, data=request.data)
        if edit_book.is_valid():
            edit_book.save()
            return Response(edit_book.data, status=status.HTTP_201_CREATED)
        else:
            return Response(edit_book.errors, status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'DELETE':
        book_data.delete()
        return Response(status=status.HTTP_200_OK)
    
    serializer = BookSerializer(book_data)
    return Response(serializer.data)