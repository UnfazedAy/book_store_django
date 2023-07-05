from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    """
    Model representing an address in the Book Outlet store.
    """
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        """
        String for representing the Address object.
        """
        return f"{self.street}, {self.postal_code} {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    """
    A class that represents an author in the Book Outlet store.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True
    )

    def full_name(self):
        """
        Returns the full name of the author.
        """
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """String for representing the Author object."""
        return self.full_name()


class Book(models.Model):
    """
    This class represents a book in the Book Outlet store.
    A book has a title, rating, author, and whether or not it is a bestseller.
    """
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)

    slug = models.SlugField(
        default="", null=False,
        blank=True, db_index=True
    )
    published_countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        """
        A method that returns the URL to access a particular book instance.
        """
        return reverse("book_detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     """
    #     A method that overrides the save method of the parent class.
    #     """
    #     self.slug = slugify(
    #         self.title)  # e.g "The Great Gatsby" -> "the-great-gatsby"
    #     super().save(*args, **kwargs)

    def __str__(self):
        """
        String for representing the Book object.
        """
        return f"{self.title} ({self.rating})"
