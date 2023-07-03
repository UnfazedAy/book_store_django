from django.shortcuts import render
from .models import Book
from django.http import Http404

# Create your views here.


def index(request):
    """
    A view that returns a list of all books in the Book Outlet store.
    """
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })


def book_detail(request, slug):
    """
    A view that returns a particular book based on its slug.
    """
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller:": book.is_bestselling,
    })
