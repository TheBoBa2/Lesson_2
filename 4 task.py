price = int(input("Введіть ціну книжки: "))
discount = int(input("Введіть розмір знижки: "))

result = price - (price * discount) / 100
print("Результат: ", result)