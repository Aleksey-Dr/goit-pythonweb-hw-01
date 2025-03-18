from abc import ABC, abstractmethod
from typing import List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        removed_books = [book for book in self.books if book.title == title]
        self.books = [book for book in self.books if book.title != title]
        for book in removed_books:
            logging.info(f"Book removed: {book}")

    def show_books(self) -> None:
        if not self.books:
            logging.info("Library is empty.")
        else:
            for book in self.books:
                logging.info(book)


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        try:
            year_int = int(year)
            book = Book(title, author, year_int)
            self.library.add_book(book)
        except ValueError:
            logging.error("Invalid year format. Please enter a valid integer.")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.error("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
