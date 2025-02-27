

class MfuPrinter:
    """
    Базовый класс мфу_принтер.
    """
    def __init__(self, name: str = None, color: str = "no", page_format: str = 'A4', model: str = None):
        """
        :param name: Имя принтера. Например: Принтер бухгалтера
        :param color: атрибут указывающий на возможность цветной печати
        :param page_format: максимально возможный формат бумаги для печати
        :param model: Модель принтера. Например: Epson-l350
        Все атрибуты доступны для чтения и записи через обьявленные свойства
        """
        self._name = name
        self._print_color = color
        self.page_format = page_format
        self.model = model

    def __str__(self) -> str:
        return f"МФУ принтер '{self.name}'"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, vol: str):
        if not isinstance(vol, str):
            raise "Параметр name должен быть строкой"
        self._name = vol

    @property
    def print_color(self):
        return self._print_color

    @print_color.setter
    def print_color(self, vol: str = 'no'):
        if isinstance(vol, str) and (vol == "yes" or vol == "no"):
            self._print_color = vol
        else:
            raise TypeError("Параметр name должен быть строкой yes или no")


class Grape:
    """
    Базовый класс Виноград.
    Представляет собой плоды винограда культурного и некоторых других
    растений рода Виноград, в зрелом виде представляющие собой сладкие ягоды.
    """
    def __init__(self, sort: str = None, color: str = None, usage: list = None):
        """
        :param sort: Сорт винограда. Например: Мускад Гамбургский
        :param color: атрибут указывающий на цвет созревшей ягоды. Может
                        принимать значения: black, green, red
        :param usage: Список вариантов использования. Например: Столовые, виноделие, сок, сушка,
                        универсальный, подвой, декоративный и т.д.
        Все атрибуты доступны для чтения и записи через обьявленные свойства
        """
        self._sort = sort
        self._color = color
        self._usage = usage

    def __str__(self) -> str:
        return f"Виноград '{self._sort}'"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._sort!r},{self._color!r},{self._usage!r})"

    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, name: str):
        if not isinstance(name, str):
            raise "Параметр sort должен быть строкой"
        self._sort = name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, vol: str):
        if isinstance(vol, str) and (vol == "black" or vol == "green" or vol == "red"):
            self._color = vol
        else:
            raise TypeError("Параметр name должен быть black, green или red")

    @property
    def usage(self):
        return self._usage

    @usage.setter
    def usage(self, vol: list):
        if isinstance(vol, list):
            self._usage = vol
        else:
            raise TypeError("Параметр не соответствует списку вариантов использования.")


class NetworkPrinter(MfuPrinter):
    """
    Дочерний класс Сетевой принтер. Отличие от родительского класса - добавлены атрибуты для
    настройки сетевого подключения.
    """
    def __init__(self, name: str = None, color: str = "no", page_format: str = 'A4', model: str = None,
                 address: str = "0.0.0.0/32", gateway: str = "0.0.0.0"):
        """
            Атрибуты из родительского класса MFU_printer:
        :param name: Имя принтера. Например: Принтер бухгалтера
        :param color: атрибут указывающий на возможность цветной печати
        :param page_format: максимально возможный формат бумаги для печати
        :param model: Модель принтера. Например: Epson-l350
            Добавлены атрибуты описывающие сетевые настройки
        :param address: Сетевой адрес и маска сети. Например: "192.168.10.232/24"
        :param gateway: Сетевой шлюз. Например "192.168.10.1"
            Все атрибуты доступны для чтения и записи через обьявленные свойства
        """
        super().__init__(name, color, page_format, model)
        self.address = address
        self.gateway = gateway

    def __str__(self) -> str:
        return f"Сетевой МФУ принтер '{self.name}'"


class PosTerminal(NetworkPrinter):
    """
        Чековый принтер (POS терминал)
    Дочерний класс от Сетевого принтера.
    В связи с спецификой конструкции убраны ненужные свойства page_format и color.
    """
    def __init__(self, name: str = None, model: str = None, address: str = "0.0.0.0/32", gateway: str = "0.0.0.0"):
        color = "no"
        page_format = 'лента'
        super().__init__(name, color, page_format, model, address, gateway)

    def __str__(self) -> str:
        return f"Сетевой POS терминал '{self.name}'"


class GrapeJuice(Grape):
    """
    Класс "Виноградный сок"
    Дочерний клаасс от класса Grape
    :param grapesort: Сорт винограда. Например: Рубиновый Магарача
    :param volume: Обьем в литрах
    :param data: Дата призводства
    :param tm: Торговая марка
    Все атрибуты доступны для чтения и записи через обьявленные свойства
    """
    def __init__(self, volume: int = 1, data: str = None, grapesort: str = None, tm: str = None):
        super().__init__(grapesort)
        self._volume = volume
        self._data = data
        self._tm = tm

# Методы __str__ и __repr__ необходимо переопределить
    def __str__(self) -> str:
        return f"Виноградный сок из винограда'{self._sort}'"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._volume}, {self._data}, {self._sort}, {self._tm!r})"

    @property
    def volume(self):
        return self._volume

    @property
    def data(self):
        return self._data

    @property
    def tm(self):
        return self._tm

    @volume.setter
    def volume(self, vol: int):
        ...
        self._usage = vol

    @data.setter
    def data(self, vol: str):
        ...
        self._data = vol

    @tm.setter
    def tm(self, vol: str):
        ...
        self._tm = vol


if __name__ == "__main__":
    my_printer = MfuPrinter(name="Принтер офиса")
    my2_printer = NetworkPrinter(name="Сетевой офисный принтер")
    my3_printer = PosTerminal(name="Сетевой POS принтер")
    print(my_printer)
    print(repr(my_printer))
    print(my_printer.__dict__)
    print("----- 2 -----")
    print(my2_printer)
    print(repr(my2_printer))
    print(my2_printer.__dict__)
    print("----- 3 -----")
    print(my3_printer)
    print(repr(my3_printer))
    print(my3_printer.__dict__)
    G1 = Grape("Кардинаk", "red", ["столовый"])
    print(G1)
    print(repr(G1))
    print(G1.__dict__)
    GJ = GrapeJuice(1,"26 июля 2025", "Изабелла", "Азбука здоровья")
#    GJ = GrapeJuice()
    print(GJ)
    print(repr(GJ))
    print(GJ.__dict__)