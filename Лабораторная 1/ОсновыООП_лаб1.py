class Pencil:
    """
    Класс Pencil описывает модель карандаша
    """
    def __init__(self, length: int, width: int, sharp: bool, color="Black"):
        """
        Инициализация обьекта конструктором
        :param color: - цвет карандаша, значение по умолчанию "Black"
        :param length: - длина карандаша. Аргумент устанавливается после валидации
        методом check_length
        :param width: - толщина карандаша, присваивется переданное конструктору значение width
        :param sharp: - аргумент указывающий на то, заточен карандаш (True), либо нет (False)
        """
        self.MIN_LENGTH = 100
        self.color = color
        self.check_length(length)
        self.width = width
        self.set_sharp(sharp)


    def check_length(self, length: int):
        # SetLength проверяет длину карандаша.
        # Метод изменяет аргумент length либо возвращает ошибку.
        # Если длина менее допустимого значения MIN_LENGTH генерируется ошибка ValueError.
        # В этом случае в конструкторе обьект не создается. Если обьект
        # уже создан, но проверка не пройдена, то эта ошибка говорит о необходимости
        # замены карандаша
        ...

    def set_sharp(self, sharp: bool):
        # Метод SetSharp проверяет тип и изменяет аргумент sharp.
        # Чтение этого аргумента позволяет определить требуется ли заточка карандаша :)
        ...


class Weather:
    """
    Класс Weather описывает модель электронной погодной станции
    Станция измеряет температуру, давление и влажность в реальном времени
    """
    def __init__(self, pressure: int, temperature: int, humidity: int):
        """
        Инициализация обьекта конструктором
        Все аргументы проходят проверку на соответсвие типа аргументов и соотвествия
        диапазону значений
        :param pressure: давление. Целое число в дипазоне от MIN_PRESSURE до MAX_PRESSURE (мм.р.с)
        :param temperature: температура. Целое число в диапазоне от MIN_TEMPERATURE до
        MAX_TEMPERATURE (С)
        :param humidity: влажность. Целое число в диапазоне от MIN_HUMIDITY до MAX_HUMIDITY (%)
        Например:
        >>> meteo_station1 = Weather(760, 20, 43)
        >>> meteo_station1.set_humidity(73)
        >>> print(meteo_station1.humidity)
        73
        """
        self.MIN_PRESSURE = 600
        self.MAX_PRESSURE = 800
        self.MIN_TEMPERATURE = -50
        self.MAX_TEMPERATURE = 60
        self.MIN_HUMIDITY = 0
        self.MAX_HUMIDITY = 100
        self.set_pressure(pressure)
        self.set_temperature(temperature)
        self.set_humidity(humidity)

    def set_pressure(self, pressure: int):
        # Метод set_pressure служит для проверки и внесение изменения в аргумент pressure
        # проводится проверка на соответсвие типа аргументов и соответствия
        # диапазону значений от MIN_PRESSURE до MAX_PRESSURE
        ...

    def set_temperature(self, temperature: int):
        # Метод set_temperature служит для внесения изменений в аргумент temperature
        # Так же проводится проверка на соответсвие типа аргументов и соотвествия
        # диапазону значений от MIN_TEMPERATURE до MAX_TEMPERATURE
        ...

    def set_humidity(self, humidity: int):
        # Метод set_humidity служит для внесения изменений в аргумент humidity
        # Так же проводится проверка на соответсвие типа аргументов и соответствия
        # диапазону значений от MIN_HUMIDITY до MAX_HUMIDITY
        if not isinstance(humidity, int):
            raise TypeError
        if not self.MAX_HUMIDITY > humidity > self.MIN_HUMIDITY:
            raise ValueError
        self.humidity = humidity


class Shirt:
    """
    Класс Shirt описывает модель мужской рубашки.
    """
    def __init__(self, color: str, size: int, clean: bool):
        """
        Инициализация обьекта Shirt
        :param color: В аргументе типа str описывается расцветка рубашки.
        :param size: Размер рубашки, целое число, две цифры
        :param clean: Аргумент clean принимает значение True если рубашка чистая, False, если рубашке
        требуется стирка
        """
        self.MIN_SIZE = 35
        self.MAX_SIZE = 50
        self.color = color
        self.set_size(size)
        self.set_clean(clean)


    def set_size(self, size: int):
        # Метод set_size служит для проверки и внесение изменения в аргумент size
        # Проводится проверка на соответсвие типа аргументов и соответствия
        # диапазону значений от MIN_SIZE до MAX_SIZE
        ...

    def set_clean(self, clean: bool):
        # Метод set_clean служит для проверки типов и внесения изменений в аргумент clean.
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
