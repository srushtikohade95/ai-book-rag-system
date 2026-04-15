from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from .models import Book
from .serializers import BookSerializer
from .scraper import scrape_books
from .rag import generate_answer


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def scrape_and_store(request):
    data = scrape_books()

    for item in data:
        Book.objects.create(**item)

    return Response({"message": "Books scraped and stored!"})


@api_view(['GET'])
def ask_book(request):
    query = request.GET.get("q")

    if not query:
        return Response({"error": "No query provided"})

    answer = generate_answer(query)

    return Response({"response": answer})


# ✅ BOOK DETAIL API (THIS WAS MISSING / NOT DETECTED)
@api_view(['GET'])
def get_book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"})


# ✅ FRONTEND VIEW
def home(request):
    return render(request, 'index.html')