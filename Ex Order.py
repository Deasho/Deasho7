User = input("Username : ")
Pass = input("Password : ")
if User == "deasho" and Pass == "26072545":
    print("___Welcome to market___")
    print("1. Vegetable >> 50 THB: ")
    print("2. Water     >> 10 THB: ")
    print("3. Banana    >> 20 THB: ")
    print("4. Chocolate >> 100 THB: ")
    Menu = int(input(""))
    if Menu == 1:
        Many = int(input("Vegetable : "))
        Price = 50
        print(Many * Price)
    elif Menu == 2:
         Many = int(input("Water : "))
         Price = 10
         print(Many * Price)
    elif Menu == 3:
         Many = int(input("Banana : "))
         Price = 20
    elif Menu == 4:
         Many = int(input("Chocolate : "))
         Price = 100
         print(Many * Price)
print("Thank you <3")

