def filter_by_state(list_input: list[dict], state="EXECUTED") -> list:
    """принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    list_output = []
    list_index = 0
    while list_index < len(list_input):
        if list_input[list_index]["state"] == state:
            list_output.append(list_input[list_index])
        list_index += 1
    return list_output


def sort_by_date(list_input: list, desc=True) -> list:
    """принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате
    (date)."""
    if desc:
        list_output = sorted(list_input, key=lambda item: item["date"], reverse=True)
    else:
        list_output = sorted(list_input, key=lambda item: item["date"], reverse=False)
    return list_output
