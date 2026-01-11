inventory = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'kiwi']
processed_items = []
for index,fruit in enumerate(inventory,start=1):
    if index%2==0 and len(fruit)>5:
        processed_items.append(f"{index}. Удлиненный {fruit}")
    elif index%2!=0 and fruit[0].lower() in "aeiou":
        processed_items.append(f"{index}. Стартует с гласной: {fruit}")
    else:
        processed_items.append(f"{index}. {fruit}")
print(inventory)
print(processed_items)