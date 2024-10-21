from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

class Publisher(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    bookID = models.IntegerField()
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    isbn = models.CharField(max_length=10)
    average_rating = models.DecimalField(decimal_places=2, max_digits=3)
    language_code = models.CharField(max_length=3)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.DateTimeField("date published")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class Member(models.Model):
    name = models.CharField(max_length=200)
