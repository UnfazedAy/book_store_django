from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    """
    This class represents a book in the Book Outlet store.
    A book has a title, rating, author, and whether or not it is a bestseller.
    """
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    def get_absolute_url(self):
        """
        A method that returns the URL to access a particular book instance.
        """
        return reverse("book_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        """
        A method that overrides the save method of the parent class.
        """
        self.slug = slugify(
            self.title)  # e.g "The Great Gatsby" -> "the-great-gatsby"
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String for representing the Book object.
        """
        return f"{self.title} ({self.rating})"
