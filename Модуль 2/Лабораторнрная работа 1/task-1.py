# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Car:
    def __init__(self, wheels_number: int, doors_number: int, is_truck: bool):
        """
        Инициализация класса

        :param wheels_number: Количество колес.
        :param doors_number: Количество дверей.
        :param is_truck: Является ли машина грузовиком.

        Пример:
        >>> car = Car(wheels_number=4, doors_number=2, is_truck=False)  # инициализация экземпляра класса
        """
        self.wheels_number = wheels_number
        self.doors_number = doors_number
        self.is_truck = is_truck

    def car_is_truck(self) -> bool:
        """
        Функция проверяющая, является ли машина грузовиком

        :return: true - является, false - нет

        Примеры:
        >>> car = Car(wheels_number=6, doors_number=2, is_truck=True)
        >>> car.car_is_truck()
        """
        ...

    def chane_wheels_number(self, number_of_wheels: int) -> None:
        """
        Меняем число колес на машине (как в большую, так и в меньшую сторону)

        :raise ValueError: Если количество колес не int, то вызываем ошибку

        :param number_of_wheels: Количество колес на которое измениться показатьель wheels_number
        :return: None

        Пример:
        >>> car = Car(wheels_number=6, doors_number=2, is_truck=True)
        >>> car.chane_wheels_number(number_of_wheels=-2)
        """
        if not isinstance(number_of_wheels, int):
            raise TypeError("Число колес должно быть типа int")
        if number_of_wheels ** 2 > self.wheels_number ** 2 and number_of_wheels < 0:
            print("Вы хотите уменьшить число колес на число большее чем колес есть!")
        ...

    def car_crashed(self) -> None:
        """
        Имитируем уничтожение автомобиля

        :return: None

        Пример:
        >>> car = Car(wheels_number=6, doors_number=2, is_truck=True)
        >>> car.car_crashed()
        """
        ...


class Phone:
    def __init__(self, battery_charge: int, free_memory: float):
        """
        Инициализация класса

        :param battery_charge: заряд батареи на данный момент
        :param free_memory: свободное место на телефоне в гигабайтах

        Пример:
        >>> phone = Phone(battery_charge=53, free_memory=25.7)
        """
        self.battery_charge = battery_charge
        self.free_memory = free_memory

    def charge(self, time: int) -> None:
        """
        Заряжаем телефон n минут
        :param time: время зарядки (минут)
        :return: None

        Пример:
        >>> phone = Phone(battery_charge=53, free_memory=25.7)
        >>> phone.charge(time=30)
        """
        if not isinstance(time, int):
            raise TypeError("Время должно быть типа int")
        if time < 0:
            print("Время - это положительное число!!!")
        ...

    def del_app(self, app_weight: float) -> None:
        """
        Удаляем приложение из памяти телефона.
        :param app_weight: Размер приложения в гигабайтах
        :return: None

        Пример:
        >>> phone = Phone(battery_charge=53, free_memory=25.7)
        >>> phone.del_app(app_weight=1.34)
        """
        if not isinstance(app_weight, (int, float)):
            raise TypeError("Размер приложения должен быть типа int или float")
        if app_weight < 0:
            print("Вес приложения не может быть отрицательным")
        ...


class Person:
    def __init__(self, age: int, weight: float, height: float):
        """
        Инициализация класса

        :param age: возраст человека (в годах)
        :param weight: вес человека (в килограммах)
        :param height: рост человека (в сантиметрах)

        Пример:
        >>> person = Person(age=5, weight=25.7, height=103.2)
        """
        self.age = age
        self.weight = weight
        self.height = height

    def growing_up(self, years: int) -> None:
        """
        Взросление человека

        :param years: на сколько лет вырос
        :return: None

        Пример:
        >>> person = Person(age=5, weight=25.7, height=103.2)
        >>> person.growing_up(years=3)
        """
        if not isinstance(years, int):
            raise TypeError("Число лет должно быть типа int")
        if years < 0:
            print("Число лет не может быть отрицательным")
        ...

    def eating(self, meal_calories: float) -> None:
        """
        Человек ест - вес растет

        :return: None

        Пример:
        >>> person = Person(age=5, weight=25.7, height=103.2)
        >>> person.eating(meal_calories=129.0)
        """
        if not isinstance(meal_calories, (int, float)):
            raise TypeError("Число калорий должно быть типа int или float")
        if meal_calories < 0:
            print("Число калорий не может быть отрицательным")
        ...

    def is_fat(self) -> bool:
        """
        Является человек толстым или все таки нет, выявляем соотноешение роста и веса

        :return: bool

        Пример:
        >>> person = Person(age=5, weight=25.7, height=103.2)
        >>> person.is_fat()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
