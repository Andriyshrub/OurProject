stationery_store = [
    'Олівець', 'Ручка', 'Обкладинка',
    'Крейда', 'Зошит', 'Абетка',
    'Гумка', 'Лінійка', 'Пенал',
    'Словник', 'Рюкзак', 'Пластилін']


def add_store():
    stationery_store.append(stationery_store.insert(0, my_tuple))
    return print(stationery_store)


while True:
    my_tuple = tuple(input('Введіть дані :').split())
    add_store()
