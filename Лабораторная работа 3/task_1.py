def search(list_, item_):
    item_index = None
    i = 0
    for item_from_list in list_:
        if item_from_list == item_:
            item_index = i
            break
        else:
            i += 1
    return item_index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
