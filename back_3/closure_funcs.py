'''
    функция с замыканиями (минимум 3 примера)
'''


def counter():
    """Возвращает функцию, считающую количество вызовов."""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment


def list_writer():
    '''Возвращает функцию, обрабатывающую список, где мы можем
    делать заметки по номеру строки и читать их'''
    list_sample = []
    index_list = []
    def list_update(index, line=""):
        if index in index_list:
            return list_sample[index_list.index(index)]
        else:
            if len(line)<1:
                return "строка пуста"
            else:
                index_list.append(index)
                list_sample.append(line)
                return list_sample[index_list.index(index)]
    return list_update


def create_prefixer(prefix):
    '''Возвращает функцию, в которой можно получить вводимую строку 
    с переданным ранее префиксом'''
    def add_prefix(word):
        return f"{prefix}{word}"
    return add_prefix
