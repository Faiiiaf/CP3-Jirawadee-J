def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Done !")
        print("----- iShop -----")
        print("1. Vat Calculator")
        print("2. Price Calculator")
def menuselect():
    userSelected = int(input("type here:"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price + (price * vat / 100)
        return result
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        return price1+price2


print(login())
print(menuselect())
print("THANK YOU:)))")




