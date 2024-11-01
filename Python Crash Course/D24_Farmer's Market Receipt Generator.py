# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
basket = [
("Peaches", 3.0, 2.99),
("Pears", 5.0, 1.66),
("Plums", 2.5, 3.99)
]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
fruit, weight, unit_price = item
subtotal += (weight * unit_price)


# Now calculate the sales tax and total bill.
#
tax_rate = 0.06625  # 6.625% sales tax in New Jersey
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
#
print("Subtotal:", subtotal)
print("Sales Tax:", tax_amt)
print("Total:", total)

def file_size(file_info):
  name, extention, size= file_info
  return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21



