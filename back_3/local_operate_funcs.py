'''
    функция, вызывающая внутри себя другую функцию
    функция, принимающая функцию как параметр (минимум 3 примера)
    функция с объявленной внутри локальной функцией (минимум 2 примера)
'''


from param_funcs import generate_tag


# Функция, вызывающая внутри себя другую функцию
def generate_random_tag():
    """Вычисляет площадь квадрата, используя функцию возведения в квадрат."""
    return generate_tag(-1, -1)


# Функция, принимающая другую функцию как параметр (3 примера)
def filter_list(unfiltered_list, filter_func):
    """Применяет заданную функцию-операцию к двум числам."""
    return filter_func(unfiltered_list)


def transform_list(items, transform_func):
    """Преобразует каждый элемент списка, используя функцию преобразования."""
    return [transform_func(item) for item in items]


def conditional_operation(a, b, condition, operation_true, operation_false):
    """Выбирает операцию в зависимости от условия и применяет её."""
    return operation_true(a, b) if condition else operation_false(a, b)


# Функция с локальной функцией (2 примера)
def is_prime(n):
    '''Функция для проверки на простое число'''
    def inner_is_prime(n, divisor):
        if divisor * divisor > n:
            return True
        if n % divisor == 0:
            return False
        return inner_is_prime(n, divisor + 1)
    if n <= 1:
        return False
    return inner_is_prime(n, 2)

def sum_list(numbers):
    '''Функция вычисления суммы элементов списка'''
    def inner_sum(numbers, index):
        if index == len(numbers):
            return 0
        else:
            return numbers[index] + inner_sum(numbers, index + 1)
    return inner_sum(numbers, 0)
