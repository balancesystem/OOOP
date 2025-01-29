from typing_extensions import Annotated
from pydantic import BaseModel, Field, constr


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book(BaseModel):
    """
    Класс Книга служит для создания обьектов книг которые будут добавляться в библиотеку
    """
    id: Annotated[int, Field(strict=True, gt=0)]  # id: - уникальный номер книги
    name: constr(strip_whitespace=True, min_length=3)  # name: - назваание книги
    pages: Annotated[int, Field(strict=True, gt=0)]  # pages: - количесво страниц


class Library(BaseModel):
    """
    Библиотека книг
    При инициализации Library должен быть пустой список|список с экземплярами класса Book
    """
    books: list[Book] = []

    """
    Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
    Если книг в библиотеке нет, то вернуть 1.
    Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.
    """
    def get_next_book_id(self) -> int:
        count_books = len(self.books)
        if count_books == 0:
            return 1
        else:
            return self.books[count_books - 1].id + 1

    """
    Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
    Если книга существует, то вернуть индекс из списка.
    Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"
    """
    def get_index_by_book_id(self, id_: int):
        for item, book in enumerate(self.books):
            if book.id == id_:
                return item
        return ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

#    list_books = [
#        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
#    ]
#    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    # добавляем книги в пустую библиотеку
    library_with_books = empty_library.model_validate({'books': BOOKS_DATABASE})
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
