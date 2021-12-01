from flask import Flask, render_template, request, redirect, Blueprint

# from models.author import Author
# from models.book import Book

from repositories import book_repository
from repositories import author_repository

books_blueprint = Blueprint("books", __name__)