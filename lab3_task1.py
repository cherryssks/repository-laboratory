# TODO Напишите функцию для поиска индекса товара


def find_index(items, item_to_find):
    try:
        return items.index(item_to_find)  # Используем метод index для поиска
    except ValueError:
        return None  # Если элемент не найден, возвращаем None

# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Список для поиска
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)
    # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")