from datetime import date

birth_year = input('Enter your birth year: ')
birth_year = int(birth_year)

age = date.today().year - birth_year

print(age)