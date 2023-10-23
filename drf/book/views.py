from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from .serializer import bookSerializer, BookTitleSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
import json
from rest_framework.views import APIView

# Create your views here.
@require_POST
def time_from_publish(request):
    """
    this view returns the time that passed from the publish date
    """
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
    
    current_time = timezone.now()
    time_diff = current_time - data['publication_date']
    days = time_diff.days
    return JsonResponse({"days": days}, status=200)



class ListBooks(APIView):
    def get(self, request, format=None):
        """
        Return a list of all books.
        """
        books = Book.objects.all()
        serializer = bookSerializer(books, many=True)
        return HttpResponse(serializer.data, status=200) 
    
    
    def post(self, request, format=None):
        """
        Create a new book.
        """
        serializer = bookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=200)
        return HttpResponse(serializer.errors, status=400)
    

class RetrieveUpdateDestroyBook(APIView):
    """
    View to retrieve, update, or delete a specific book.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    def get(self, request, pk, format=None):
        """
        Retrieve a specific book by primary key.
        """
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

        serializer = bookSerializer(book)
        return HttpResponse(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update a specific book by primary key.
        """
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return HttpResponse({"error": "Book not found"}, status=404)

        serializer = bookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)
        return HttpResponse(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        """
        Delete a specific book by primary key.
        """
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

        book.delete()
        return JsonResponse(status=200)

    

class UpdateBookTitleView(APIView):
    def post(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return HttpResponse({"error": "Book not found"}, status=404)

        serializer = BookTitleSerializer(data=request.data)

        if serializer.is_valid():
            new_title = serializer.validated_data['title']
            book.title = new_title
            book.save()
            return HttpResponse({"message": "Title updated successfully"}, status=200)
        else:
            return HttpResponse(serializer.errors, status=400)