nums = list(range(1,21))
nums_odd = list(filter(lambda num: num%2!=0 , nums))
result = list(map(lambda  num: num**3 , nums_odd))

print(result)