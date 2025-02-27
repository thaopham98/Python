from datetime import date

todays_date = date.today()

def cal_age(birthyear: int, name: str):
    # todays_date = date.today()
    cYear = todays_date.year
    age = cYear - birthyear
    print(name, 'is', age, 'years old.')

cal_age(1998, 'Thao Pham')

Name = input('\nEnter your name:')
bYear = int(input('Enter your birthyear:'))
cal_age(bYear, Name)
    