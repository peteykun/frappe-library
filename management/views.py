from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Book, Member

# Index
def index(request):
    return HttpResponse("Hello, world. You're at the management index.")

# Members
def members(request):
    members = Member.objects
    template = loader.get_template("members/index.html")
    context = {
        "members": members,
    }
    return HttpResponse(template.render(context, request))

def member(request, member_id):
    return HttpResponse("You're looking at member %s." % member_id)

# Books
def books(request):
    books = Book.objects
    template = loader.get_template("books/index.html")
    context = {
        "books": books,
    }
    return HttpResponse(template.render(context, request))

def book(request, book_id):
    return HttpResponse("You're voting on book %s." % book_id)
