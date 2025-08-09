from django.db import models
from datetime import date

# Author model - one author can have many books
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name


# Book model - belongs to an Author
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year published
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )  # One-to-many relationship

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

# Create your models here.
