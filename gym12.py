from string import ascii_letters
# 1)стр: импортируем из библиотеки string набор латинского алфавита
class Person:
    # 2) стр: создаем класс
    S_RUS = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    # 3) стр: создаем свойство класса и вносим в него все русские бкувы и знак дефиса
    S_RUS_UPPER = S_RUS.upper()
    # 4) стр: создаем свойство присваеваем ему значение стр.3 но применяем к ней метод .upper
    def __init__(self, name, old, passport, weight):
        # 5) стр: метод инициализации объектов класса
        self.verify_old(old)
        self.verify_passport(passport)
        self.verify_weight(weight)
        self.verify_name(name)
        # строки 6,7,8,9) вызывают методы проверки корректности введенных данных
        self.__name = name.split()
        self.__old = old
        self.__passport = passport
        self.__weight = weight
        # строки 10,11,12,13) ссылки на аргументы объектов класса
    @classmethod
    # 14) стр: создаем метод класса
    def verify_name(cls, name):
        # 15) стр: указываем метод проверки имени (сls - ссыдка на класс, name - аргумент который будем проверять)
        if type(name) != str:
            # 16) стр: условие если тип аргумента name не является строкой
            raise TypeError("Неправильный тип данных ")
            # 17) стр: сообщение об ошибке
        n = name.split()
        # 18) стр: создаем переменную присваиваем ей значение аргумента и указываем команду разделить по пробелам
        if len(n) != 3:
            # 19) стр: условие проверки: если количество елементов в строке не равно 3
            raise TypeError('неверный формат записи')
            # 20) стр: сообщение об ошибке
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        # 21) стр: создаем переменную присваиваем ей ранее созданные или импортированые аргументы (латинский большой и маленький русский алфаит и дефис)
        for s in n:
            # 22) стр: цикл фор
            if len(s) < 1:
                # 23) стр: условие проверки если длина меньш.1
                raise TypeError('В ФИО должен быть хотя бы 1 символ')
                # 24) стр: сообщение об ошибке
            if len(s.strip(letters)) != 0:
                #25) стр: s.strip отнимает из s символы которые есть в letters в результате если мы правильно указали
                #ФИО то результат отнимания будет ноль. условие проверкиЖ если к-во элементов в результате отнимания не равно 0
                raise TypeError('ФИО содержит недопустимый смвол')
                # 26) стр: сообщение об ошибке
    @classmethod
    # 27 стр: создаем метод класса
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            # условие проверки если типо аргумента не целое а значение менш. 14 и болш.120
            raise TypeError('Возраст должен быть целым числом в диапазоне [14;120]')
    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            # условие проверки если тип аргумента не вещественное число а значение меньше 20
            raise TypeError('Вес должен быть вещественным числом больше 20')

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            # усл.пр: если тип аргумента не строка
            raise TypeError("Серия паспорта должна быть в формате строки")
        s = passport.split()
        # создаем переменную указываем что к ней нужно применить сплит по пробелу
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            # если количество элементов не равно двум или длина строки первого эл не равна 4 или длина стр 2 эл не равна 6
            raise TypeError('Неверный формат паспорта')

        for p in s:
            # создаем цикл
            if not p.isdigit():
                # isdigit возвращает True если р состоит только из цифр, условие: если не True будет ошибка
                raise TypeError('Серия и номер должны быть цифрами')
    @property
    def name(self):
        return self.__name
    # геттер дя имени
    @property
    def old(self):
        return self.__old
    # геттер для возраста
    @old.setter
    def old(self, old):
        #сеттер для возраста
        self.verify_old(old)
        #ссылка на проверку правильности данных
        self.__old = old
    @property
    def passport(self):
        return self.__passport
    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

p = Person('Павлов Александр андреевич', 25, "1234 123456", 57.0 )