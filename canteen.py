menu ={ 
    'Pizza': 80,
    'Pasta': 50,
    'Coffee': 20,
    'Burger': 40,
    'Salad': 50,
    'Tea': 10,

}

print("-----Welcome to THAPAR canteen------ ")
print("\n----------Menu----------")


for item, price in menu.items():
 print(item, ":Rs", price)

order_total= 0
bill= {} 

while True: 

 item = input("\nEnter the name of item you want to order= ").title()
 if item in menu:
    qty = int(input("Enter quantity:"))
    order_total += menu[item] * qty
    if item in bill:
       bill[item] += qty
    else:
       bill[item]= qty
    print(qty , item , "has been added to your order")

 else:
   print("Your order", item, "is not in the menu")


 another_order= input("Do you want to order anything else? (yes/no) ").lower()

 if another_order == "no":
        break
 elif another_order != "yes":
        print("Invalid input. Order ended.")
        break
    
        
print("\n------Bill-------")
for item, qty in bill.items():
 print(item, "*", qty, "=Rs", menu[item] * qty)

print("----------------------")


print("Total amount= Rs", order_total)  
print("\nThank you for ordering!")
