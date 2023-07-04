from django.shortcuts import render
from .models import Book
from django.http import Http404, HttpResponse
from django.db.models import Avg
from typing import Union

# Create your views here.


def index(request):
    """
    A view that returns a list of all books in the Book Outlet store.
    """
    books = Book.objects.all().order_by("title")  # QuerySet of all books
    total_books = books.count()  # Total number of books
    avg_rating = books.aggregate(Avg("rating"))  # Average rating of all books

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": total_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug: str) -> Union[HttpResponse, Http404]:
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
