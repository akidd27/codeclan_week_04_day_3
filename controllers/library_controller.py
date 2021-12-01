from flask import Flask, render_template, request, redirect, Blueprint

# from models.author import Author
# from models.book import Book

from repositories import book_repository
from repositories import author_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

@books_blueprint.route("/books/<id>/delete", methods = ["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")