from datetime import date

sub_total = 0
price = 1
quantity = 0
today = date.today()
# week_day = today.weekday()
week_day = 2
discount = 0

def taxes_n_total(sub_total):
    taxes = sub_total * 0.06
    total = sub_total + taxes
    return taxes, total

while price != 0:
    price = float(input('What is the price of the product by unit? (Enter 0 to end): '))
    if price == 0:
        break
    else:
        quantity = int(input('How much units are you buying?: '))
        sub_total = sub_total + price * quantity

if (week_day == 1 or week_day == 2) and sub_total >= 50:
    discount = sub_total * 0.10
    sub_total = sub_total - discount
    taxes, total = taxes_n_total(sub_total)
    print('''Discount amount: {:.2f}
Sales tax amount: {:.2f}
Total: {:.2f}'''.format(discount, taxes, total))

elif (week_day == 1 or week_day == 2) and sub_total <= 50:
    difference = 50 - sub_total
    sub_total = sub_total - discount
    taxes, total = taxes_n_total(sub_total)
    print('''You have to purchase {:.2f} more in products to get a 10% discount.
Sales tax amount: {:.2f}
Total: {:.2f}'''.format(difference, taxes, total))
    
else:
    taxes, total = taxes_n_total(sub_total)
    print('''Sales tax amount: {:.2f}
Total: {:.2f}'''.format(taxes, total))
