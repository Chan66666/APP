import calendar
from datetime import date
today = date.today()
current_year = today.year
current_month = today.month
print(calendar.month(current_year, current_month))
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
print(calendar.month(year, month))
option = input("Enter 'prev' to see the previous month, 'next' to see the next month, or 'quit' to exit: ")

if option == 'prev':
    current_month -= 1
    if current_month == 0:
        current_month = 12
        current_year -= 1
elif option == 'next':
    current_month += 1
    if current_month == 13:
        current_month = 1
        current_year += 1
elif option == 'quit':
    break

print(calendar.month(current_year, current_month))

