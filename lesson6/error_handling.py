data = {"price": "10.5", "id": "abc"}
def get_as_float(data_dict, key):
    try:
        data_dict[key] = float(data_dict[key])
    except ValueError:
        print(f"Ошибка: Значение по ключу '{key}' нельзя превратить в число!")
    except KeyError:
        print(f"Ошибка: Ключ '{key}' не найден!")
    else:
        print(f"Успех: Получено число {data_dict[key]}")

get_as_float(data, "price")
get_as_float(data, "id")
get_as_float(data, "amount")