shopping_list = ['молоко', 'хлеб', 'яйца', 'сыр', 'масло']
shopping_list.append('сок')
shopping_list.insert(1, 'йогурт')

i = shopping_list.index('хлеб')
shopping_list[i] = 'батон'

shopping_list.remove('масло')

print(f'{shopping_list[0]},{shopping_list[-1]}')
print(shopping_list[2:5])

shopping_list.sort()
print(shopping_list)
print(f'Длина списка покупок: {len(shopping_list)}')
