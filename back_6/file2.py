'''
   1. 7 файлов, в каждом из которых объявлено от 3 разных функций.
    Эти функции МОГУТ реализовывать любой алгоритм.
    В каждом из файлов ДОЛЖНЫ импортироваться функции из других файлов.
    Импорт из файлов в итоге должен представлять собой древовидную структуру,
    где в файле №1 импортируются функции из файла №2, в файле №2 из файла №3 и т.д.
    Минимальный уровень глубины импортов - 3. 
'''

from file3 import station_14

def station_15():
    '''Проезд по 15 станциям МЦД-3 со стороны Каз. напр.'''
    station_14()
    print("Вы проезжаете до следующей станции.")
    print("Вы на станции Косино")

def station_16():
    '''Проезд по 16 станциям МЦД-3 со стороны Каз. напр.'''
    station_15()
    print("Вы проезжаете до следующей станции.")
    print("Вы на станции Выхино")

def station_17():
    '''Проезд по 17 станциям МЦД-3 со стороны Каз. напр.'''
    station_16()
    print("Вы проезжаете до следующей станции.")
    print("Вы на станции Вешняки")