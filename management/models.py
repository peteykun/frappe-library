from django.db import models
from hashlib import md5

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
    stock = models.IntegerField(default=1)

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)

    @property
    def email_md5(self):
        return md5(self.email.encode('utf-8'))

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

class Issuance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    rent_fee = models.DecimalField(decimal_places=2, max_digits=8)
    returned = models.BooleanField(default=False)

class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
