from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

class Publisher(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    bookID = moodels.IntegerField()
    title = models.CharField(max_length=200)
    authors = model.ManyToManyField(Author)
    isbn = models.CharField(max_length=10)
    average_rating = models.DecimalField(decimal_places=2, )
    language_code = models.CharField(max_length=3)
    num_pages = moodels.IntegerField()
    ratings_count = moodels.IntegerField()
    text_reviews_count = moodels.IntegerField()
    publication_date = models.DateTimeField("date published")
    publisher = model.ForeignKey(Publisher, on_delete=models.CASCADE)

class Member(models.Model):
    name = models.CharField(max_length=200)
