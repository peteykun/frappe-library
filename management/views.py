from django.shortcuts import render, get_object_or_404
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

def create_member(request):
    template = loader.get_template("members/create.html")
    return HttpResponse(template.render())

def show_member(request, member_id):
    return HttpResponse("You're looking at member %s." % member_id)

def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, "members/edit.html", {"member": member})

def delete_member(request, member_id):
    return HttpResponse("Deleting: member %s." % member_id)

# Books
def books(request):
    books = Book.objects
    template = loader.get_template("books/index.html")
    context = {
        "books": books,
    }
    return HttpResponse(template.render(context, request))

def create_book(request):
    template = loader.get_template("books/create.html")
    return HttpResponse(template.render())

def show_book(request, book_id):
    return HttpResponse("You're voting on book %s." % book_id)

def edit_book(request, book_id):
    return HttpResponse("Editing: book %s." % book_id)

def delete_book(request, book_id):
    return HttpResponse("Deleting: book %s." % book_id)
