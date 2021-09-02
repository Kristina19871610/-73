# Задание 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками.
card_number = '1234123456785678'
card = card_number


def card_number(card):
    print('*' * len(card[:-4]) + card[-4:])  # с помощью среза заменили все символы кроме последних четырех на *


# Задание 2. Напишите функцию, которая проверяет: является ли слово палиндромом.
Word = ' Анна '


def check_if_palindrome(string):
    prepared_str = string.replace(' ', '').lower()  # удаляем пробелы, переводим в нижний регистр

    if prepared_str == prepared_str[::-1]:  # с помощью среза с перевернули слово,если слово
        # равно перевернутому, возвращаем True иначеFalse
        return True
    else:

        return False


if __name__ == '__main__':  # выполняем проверку и печатаем
    for item in Word:
        print('Слово является палиндромом:', check_if_palindrome(item))


# Задача 3. Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай
class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}  # стадии созревания помидора

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):  # проверка, созрел ли помидор
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num):  # список из объектов класса Tomato
        self.tomatoes = [Tomato(index) for index in range(0, num - 1)]

    def grow_all(self):  # переводим все томаты из списка на следующий этап созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):  # проверяем все ли помидоры созрели
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):  # собираем урожай
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):  # выдаем садовнику растение
        self.name = name
        self._plant = plant

    def work(self):  # ухаживаем за растением
        print('Садовник работает.')
        self._plant.grow_all()
        print('Садовник закончил работу.')

    def harvest(self):  # Собираем урожай
        print('Садовник собирает урожай.')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая закончен.')
        else:
            print('Томаты еще не дозрели, продолжайте ухаживать за ними.')

    @staticmethod  # Статический метод (выводит справку по садоводству)
    def knowledge_base():
        print('''Это справка по садоводству: урожай нужно собирать когда томаты дозрели.''')


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Садовник', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
