from django.contrib import admin

# Register your models here.
from .models import Author, Publisher, Book, Member

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Member)