'''
   1. 7 файлов, в каждом из которых объявлено от 3 разных функций.
    Эти функции МОГУТ реализовывать любой алгоритм.
    В каждом из файлов ДОЛЖНЫ импортироваться функции из других файлов.
    Импорт из файлов в итоге должен представлять собой древовидную структуру,
    где в файле №1 импортируются функции из файла №2, в файле №2 из файла №3 и т.д.
    Минимальный уровень глубины импортов - 3. 
'''

def current_station():
    '''Начальная станция МЦД-3 со стороны Каз. напр.'''
    print("Вы на станции Ипподром (47 км)")

def station_1():
    '''Проезд по 1 станции МЦД-3 со стороны Каз. напр.'''
    current_station()
    print("Вы проезжаете до следующей станции.")
    print("Вы на станции Раменское")

def station_2():
    '''Проезд по 2 станциям МЦД-3 со стороны Каз. напр.'''
    station_1()
    print("Вы проезжаете до следующей станции.")
    print("Вы на станции Фабричная")
