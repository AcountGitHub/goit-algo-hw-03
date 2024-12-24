from datetime import datetime


"""
Функція повертає ціле число, яке вказує на кількість днів від заданої дати
до поточної. Якщо задана дата пізніша за поточну, результат від'ємний.
Якщо задано неправильний формат дати, функція повертає рядок з повідомленням
"""
def get_days_from_today(date):
    result = None
    try:
        date_from_string = datetime.strptime(date, "%Y-%m-%d").date()
        result = (datetime.today().date() - date_from_string).days
    except ValueError:
        result = "The date format must be YYYY-MM-DD"
    return result


print("Calculating the number of days from a given date to the current date")
date = input("Please enter the date in the format YYYY-MM-DD: ")
result = get_days_from_today(date)
if type(result) == int:
    print(f"Number of days = {result}")
else:
    print(result)