class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        :param name: Параметр содержит название книги
        :param author: Параметр содержит автора книги
        Атрибуты _name и _autor не имеют свойтсв setter и не подлежат изменениям
        """
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    """
    Класс описывающий модель бумажной книги из родительского класса Book
    """
    def __init__(self, name: str, author: str, pages: int):
        """
        :param name: наследуется из родительского класса
        :param author: наследуется из родительского класса
        :param pages: содержит количество страниц в книге
        """
        super().__init__(name, author)
        self._pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, vol: int):
        if not isinstance(vol, int):
            raise TypeError("Количество страниц должно быть числом")
        if vol < 3:
            raise ValueError("Количество страниц должно быть более 3")
        self._pages = vol


class AudioBook(PaperBook):
    """
    Класс описывающий модель электронной книги книги из родительского класса PaperBook
    """
    def __init__(self, name: str, author: str, pages: int, duration: float):
        """
        :param name: наследуется из родительского класса
        :param author: наследуется из родительского класса
        :param pages: наследуется из родительского класса
        :param duration: Время звучания аудикниги
        """
        super().__init__(name, author, pages)
        self._duration = duration

    def __str__(self):
        return f"{PaperBook(self.name, self.author, self.pages)}. Время звучания: {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages}," \
               f" duration={self._duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, vol: float):
        if not isinstance(vol, float):
            raise TypeError("Время звучания должно быть числом")
        self._duration = vol


test = AudioBook("test name", "test autor", 77, 88)
print(test)
print(repr(test))
