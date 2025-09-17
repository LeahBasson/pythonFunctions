# Function that calculates the VAT to be paid on the price an item.
# Ask the user to input the name of an item and price of the item.
# Use the VAT function to calculate and display the total price of the item.

item_name = input("Enter item: ")
item_price = int(input("Enter price: "))

def vat_cal(name="None",price=0):
    vat = item_price*0.15
    return print("item name: ",item_name, "\ntotal price: ", vat + item_price)

vat_cal(item_name,item_price)
