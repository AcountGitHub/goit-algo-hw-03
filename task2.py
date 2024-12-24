from random import sample


"""
Функція генерує вказану кількість унікальних чисел в заданому діапазоні.
Функція повертає список випадково вибраних, відсортованих чисел.
Числа в наборі не повторюються. Якщо параметри не відповідають
заданим обмеженням, функція повертає пустий список
"""
def get_numbers_ticket(min, max, quantity):
    result_list = list()
    try:
        if 1 <= min < max and max <= 1000 and min <= quantity <= max:
            result_list.extend(sorted(sample(range(min, max + 1), quantity)))
    except TypeError:
        print("Minimum value, maximum value and quantity must be integer numbers")
    return result_list


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)