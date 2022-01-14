from datetime import date

sub_total = float(input('Please enter the subtotal: '))
today = date.today()
week_day = today.weekday()
discount = 0

if (week_day == 1 or week_day == 2) and sub_total >= 50:
    discount = sub_total * 0.10
    sub_total = sub_total - discount
    taxes = sub_total * 0.06
    total = sub_total + taxes
    print('''Discount amount: {:.2f}
Sales tax amount: {:.2f}
Total: {:.2f}'''.format(discount, taxes, total))
    
else:
    taxes = sub_total * 0.06
    total = sub_total + taxes
    print('''Sales tax amount: {:.2f}
Total: {:.2f}'''.format(taxes, total))