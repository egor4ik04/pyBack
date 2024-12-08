'''
    Файл с функциями и классами для пунктов 2-9
'''

import random
import math
import locale
import decimal
import dataclasses
from file1 import station_20

# 2. Функция, в которой демонстрируется работоспособность импортов из п. 1
def module_file_test():
    '''Проезд по станциям МЦД-3 до МЦК'''
    station_20()
    print("Доступна пересадка на МЦК.")


# 3. Файлы байт-кода любых 7 модулей, написанных в течение курса
# (в том числе модулей этой лабораторной).
# Данные файлы генерирует питон при компиляции кода (модулей в байт-код).
# Они расположены в папке __pycache__, но в репозтории её нет
# в соответствии с настройкой файла .gitignore. Для локальной компиляции
# достаточно запустить программу.


# 4. Минимум 2 функции, использующие разные методы из модуля random
def generate_password(length: int = 8):
    '''Генерирует случайный пароль указанной длины из букв, цифр и символов.'''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    password = ''.join(random.choices(chars, k=length))
    return password


def random_selection(items: list, count: int):
    '''Возвращает случайный набор из указанного числа элементов списка.'''
    if count > len(items):
        raise ValueError("Элементов меньше выборки.")
    random.shuffle(items)
    return items[:count]


# 5. Минимум 3 функций, использующих разные методы из модуля math
def calculate_hypotenuse(a: float, b: float):
    '''Вычисляет длину гипотенузы прямоугольного треугольника.'''
    return round(math.hypot(a, b), 2)


def degrees_to_radians(degrees: float):
    '''Преобразует угол из градусов в радианы и возвращает радианы.'''
    radians = math.radians(degrees)
    return radians


def sin_and_cos_from_radians(radians: float):
    '''Возвращает синус и косинус указанного в радианах угла.'''
    sin = math.sin(radians)
    cos = math.cos(radians)
    return sin, cos


# 6. Минимум 3 функции, использующие разные методы из модуля locale
def set_locale_and_get_name(locale_name: str):
    '''Устанавливает указанную локаль и возвращает её имя.'''
    locale.setlocale(locale.LC_ALL, locale_name)
    return locale.getlocale()


def format_number_with_locale(number: float):
    '''Форматирует число с учетом локали для отображения.'''
    return locale.format_string("%.2f", number, grouping=True)


def format_currency_with_locale(amount: float, locale_name: str):
    '''Форматирует сумму в валюте с учётом локали.'''
    locale.setlocale(locale.LC_MONETARY, locale_name)
    return locale.currency(amount)


# 7. Минимум 2 функции, использующие разные методы из модуля decimal
def set_precision_and_add(a: float, b: float, precision: int):
    '''Устанавливает точность вычислений и выполняет сложение с заданной точностью.'''
    decimal.getcontext().prec = precision
    result = decimal.Decimal(a) + decimal.Decimal(b)
    return result


def format_decimal_to_string(number: float, decimal_places: int):
    '''Форматирует число с плавающей точкой в строку с заданным количеством знаков после запятой.'''
    number_decimal = decimal.Decimal(number)
    formatted_number = f"{number_decimal:.{decimal_places}f}"
    return formatted_number


# 8. Минимум 3 разных data-класса
@dataclasses.dataclass
class GameCharacter:
    '''Игровоц персонаж'''
    name: str
    health: int
    mana: int


@dataclasses.dataclass
class InventoryItem:
    '''Предмет инвентаря'''
    item_name: str
    quantity: int
    weight: float


@dataclasses.dataclass
class Skill:
    '''Навык'''
    skill_name: str
    level: int
    experience: float


# 9. Минимум 5 функций, использующих data-классы
# 9.1 Передача объекта data-класса как параметр
def describe_character(character: GameCharacter):
    '''Возвращает строку с описанием персонажа.'''
    return f"у {character.name} {character.health} ХП и {character.mana} МП."


# 9.2 Работа со списком из объектов data-классов
def total_inventory_weight(inventory: list[InventoryItem]):
    '''Вычисляет общий вес всех предметов в списке.'''
    return sum(item.quantity * item.weight for item in inventory)


# 9.3 Работа со словарём, где значение — объект data-класса
def get_skill_levels(skill_dict: dict[str, Skill]):
    '''Возвращает словарь с именами навыков и их уровнями.'''
    return {key: skill.level for key, skill in skill_dict.items()}


# 9.4 Модификация значений объекта data-класса
def level_up_skill(skill: Skill, levels: int):
    '''Повышает уровень навыка на указанное значение.'''
    skill.level += levels
    skill.experience = 0.0
    return skill


# 9.5 Создание объекта data-класса на основе передаваемых параметров
def create_character(name: str, health: int, mana: int):
    '''Создаёт объект персонажа на основе переданных параметров.'''
    return GameCharacter(name, health, mana)
