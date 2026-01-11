cities = input("Введите пять городов через запятую ").split(',')
for i in range(1,6):
    if "a" in cities[i-1].lower():
        print(f"Город {i}: {cities[i-1]} (в этом городе есть 'a')")
    else:
        print(f"Город {i}: {cities[i-1]}")
