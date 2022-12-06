import random
import sys


def checking_numbers(string):
    # Функция для проверки цифр в строке
    string = string.replace(" ", "")
    string = string.replace("-", "")
    try:
        int(string)
        return True
    except ValueError:
        return False


def sorted_list(list_a):
    # Быстрая сортировка Хоара
    if len(list_a) > 1:
        x = list_a[random.randint(0, len(list_a) - 1)]
        low = [u for u in list_a if u < x]
        eq = [u for u in list_a if u == x]
        hi = [u for u in list_a if u > x]
        list_a = sorted_list(low) + eq + sorted_list(hi)

    return list_a


def left_border(L, key):
    # Устанавливается номер позиции элемента, который меньше введенного пользователем числа
    left = -1
    right = len(L)
    while right - left > 1:
        middle = (left + right) // 2
        if L[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_border(L, key):
    # Устанавливается номер позиции элемента, который следующий за ним больше или равен этому числу
    left = -1
    right = len(L)
    while right - left > 1:
        middle = (left + right) // 2
        if L[middle] <= key:
            left = middle
        else:
            right = middle
    return right


sequence_numbers = input("введите последовательность чисел через пробел: ")
user_number = int(input("введите любое число: "))

if " " not in sequence_numbers:
    sys.exit("Последовательность чисел введена без пробела или вы ввели одно число!")
if not checking_numbers(sequence_numbers):
    sys.exit("Ваши вводные данные не соответствуют условию ввода!")
else:
    sequence_numbers = list(map(int, sequence_numbers.split()))

sequence_numbers = sorted_list(sequence_numbers)

print(f"Отсортированный по возростанию список пользователя: \n{sequence_numbers}")
print(f"Число пользователя: {user_number}")

y = left_border(sequence_numbers, user_number)
if y == -1 or user_number > (sequence_numbers[len(sequence_numbers) - 1] + 1):
    print("Число введеное пользователем не соответствует заданному условию")
else:
    print(f"Номер позиции элемента, который меньше введенного пользователем числа: {y}")


i = right_border(sequence_numbers, user_number)
if user_number < sequence_numbers[0] - 1 or user_number > sequence_numbers[len(sequence_numbers) - 1]:
    print("Число введеное пользователем не соответствует заданному условию")
elif user_number == sequence_numbers[len(sequence_numbers) - 1]:
    print(f"Число введенное пользователем равно последнему элементу в списке: {i}")
else:
    print(f"Номер позиции элемента, который следующий за числом пользователя больше или равен этому числу: {i}")
