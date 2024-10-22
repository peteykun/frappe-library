from django.urls import path

from . import views

urlpatterns = [
    # /management
    path("", views.index, name="index"),
    # /books/<book_id>
    path("books", views.books, name="books"),
    path("books/<int:book_id>", views.book, name="book"),
    # /books/<member_id>
    path("members", views.members, name="members"),
    path("members/<int:member_id>", views.member, name="member"),
]
