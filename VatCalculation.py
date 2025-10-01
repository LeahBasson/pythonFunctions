# Function that calculates the VAT to be paid on the price an item.
# Ask the user to input the name of an item and price of the item.
# Use the VAT function to calculate and display the total price of the item.

def vat_cal(price=0):
    vat = item_price*0.15
    total = vat + item_price
    return vat,total

item_name = input("Enter item: ")
item_price = float(input("Enter price: "))

vat, total = vat_cal(item_price)

print("\nReceipt")
print("Item:", item_name)
print("Price: R", item_price)
print("Vat:", round(vat,2))
print("Total price: R", round(total,2))