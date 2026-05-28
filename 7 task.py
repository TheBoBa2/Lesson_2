while True:
    user_input = int(input("Введіть чотирьох значне число: "))
    length = len(str(user_input))

    if length != 4 or user_input < 0:
        print("Невірне значення, попробуйте знову")
    else:
        break
print(user_input // 1000)
print(user_input // 100  % 10)
print(user_input // 10 % 10)
print(user_input % 10)