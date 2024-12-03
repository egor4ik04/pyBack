'''
    лямбда-выражение без параметров
    лямбда-выражение с параметрами
    функция, принимающая лямбда-выражение как параметр, 
        и вызывающая лямбда-выражение внутри себя
'''


# Лямбда-выражение без параметров
def get_no_param_lambda():
    '''Функция возврата лямбды без параметров'''
    return lambda: print("Привет от лямбды!")
# т.к. линтер не даёт привязать лямбда-функцию к переменной
# без ошибок, то я буду передавать её через специальную
# функцию, а там уже запускать через переменную


# Лямбда-выражение без параметров
def create_multiplier(factor):
    '''Создает лямбда-функцию, которая умножает число на заданное значение'''
    return lambda x: x * factor
# то же решение, что и выше


# Функция, принимающая лямбда-выражение как параметр
def process_value(value, func):
    """Обрабатывает значение с помощью переданной лямбда-функции."""
    return func(value)