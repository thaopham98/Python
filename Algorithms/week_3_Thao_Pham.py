account_number = int(input('\nEnter your account number: '))
service_code = input('Enter your service code (r/p): ')

def serviceType(account_input, service_code_input):
    try:
        if service_code_input.lower() == 'r':
            minute = int(input('Enter Minutes: '))
            if minute < 50:
                amount_due = 10
            else:
                amount_due = 10 + 0.2 * (minute - 50)
            
            print('\nYour account number: ', account_input)
            print('\nYour service code: Regular')
            print('\nAmount Due: $', amount_due, sep='')
        elif service_code_input.lower() == 'p':
            dayMinute = int(input('Enter Daytime minute: '))
            nightMinute = int(input('Enter Nighttime minute: '))

            if dayMinute < 75:
                day_amount = 25
            else:
                day_amount = 25 + 0.1 * (dayMinute - 75)
            
            if nightMinute < 100:
                night_amount = 25
            else:
                night_amount = 25 + 0.05 * (nightMinute - 100)

            amount_due = day_amount + night_amount

            print('\nYour account number: ', account_input)    
            print('\nYour service code: Premium')
            print('\nAmount Due: $', amount_due, sep='')
         
            # raise invalid_input1('wrong input')
    except invalid_input1:
        print('\nYou enter invalid input')

# try:
#     serviceType(account_number, service_code)
# except invalid_input as e:
#     # print('\nYou enter invalid input')
#     print(e)

serviceType(account_number, service_code)