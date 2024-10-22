from django.urls import path

from . import views

urlpatterns = [
    # /management
    path("", views.index, name="index"),
    # /books/<book_id>
    path("books", views.books, name="books"),
    path("books/new", views.create_book, name="create_book"),
    path("books/<int:book_id>", views.show_book, name="show_book"),
    path("books/<int:book_id>/edit", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete", views.delete_book, name="delete_book"),
    # /books/<member_id>
    path("members", views.members, name="members"),
    path("members/new", views.create_member, name="create_member"),
    path("members/<int:member_id>", views.show_member, name="show_member"),
    path("members/<int:member_id>/edit", views.edit_member, name="edit_member"),
    path("members/<int:member_id>/delete", views.delete_member, name="delete_member"),
]
