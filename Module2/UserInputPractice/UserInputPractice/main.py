option_price = 0
delivery_free = 4

name = input("enter your name:")
print("Hi " + name + " how are you doing today?")

specials = input("1. Burger 8$ \n 2. Pizza $5 \n 3. Fries $3")

if specials == "1":
    option_price = 8
    print("You've selected burger")
elif specials == "2":
    option_price = 5
    print("Pizza it is")
elif specials == "3":
    option_price = 3
    print("Fries all day")

confirm_delivery = input("delivery?")
if confirm_delivery == "y":
    print("total = " + str(option_price + delivery_free))
else:
    print("total: " + str(option_price))