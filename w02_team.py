# discount.py

#On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.

from datetime import datetime
current_date_and_time = datetime.now()

#for day testing enable line below
day_of_week = 2

#day_of_week = current_date_and_time.weekday()

print(day_of_week)

if day_of_week == 1 or day_of_week == 2:
    subtotal = float(input("Please enter the subtotal: "))
    discount = subtotal * 0.10 
    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax
    print(f"Discount amount: {discount:.2f} \n Sales tax amount: {sales_tax:.2f} \n Total: {total} ")

else:
    subtotal = float(input("Please enter the subtotal: "))
    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax
    print(f"Sales tax amount: {sales_tax:.2f} \n Total: {total} ")
