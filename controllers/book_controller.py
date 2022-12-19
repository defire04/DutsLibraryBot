from typing import List

from controllers.query_controller import QueryController
from models.book import Book
from services.book_service import BookService


class BookController:

    @staticmethod
    def insert(book):
        BookService.insert(book)

    @staticmethod
    def find_by_title(title):
        return BookController.result_to_list(BookService.find_by_title(title))

    @staticmethod
    def find_books_by_book_category(category_id):
        return BookController.result_to_list(BookService.find_books_by_book_category(category_id))

    @staticmethod
    def find_by_title_and_create_query(title):
        books = BookController.find_by_title(title)
        query_id = QueryController.create(title, books)
        return {
            "books": books,
            "query_id": query_id
        }
    @staticmethod
    def find_book_by_ids(request_books):
        return BookController.result_to_list(BookService.find_book_by_ids(request_books))

    @staticmethod
    def replace_c():
        BookService.replace_c()

    @staticmethod
    def clean_dataset():
        BookService.clean_dataset()

    @staticmethod
    def finalize():
        BookService.finalize()

    @staticmethod
    def result_to_list(find_result):
        books: List[Book] = []

        for book in find_result:
            books.append(Book.create_book(*book))

        return books