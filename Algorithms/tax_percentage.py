# tax = 10
# price = 100

# final_price = price * (tax/100)
# print(f'Final Price: {final_price}')

# priceTax = 10 # the price of tax 

# taxPercent = price/priceTax # x%
# print(f'Tax %: {taxPercent}%')

price1 = 16.97
price2 = 16.97+6.99
price3 = 16.97 - 1.19
price4 = 39.37
price5 = price4 - 1.19 # $38.18
est_tax_amount = 2.96

price = 13 # $
tax_percent = 7.76 # %
est_tax = 4.59 # $
"""Estimated tax amount"""
def tax_amount(price, tax_percentage):
    return round((price*tax_percentage)/100,2)
print(f'Estimated tax amount: ${tax_amount(price, tax_percent)}')

"""Tax Percentage"""
# def tax_percentage(price, tax_amount):
#     return round((tax_amount/price)*100,2)

# print(f'Tax Percentage: {tax_percentage(price,est_tax)}%')