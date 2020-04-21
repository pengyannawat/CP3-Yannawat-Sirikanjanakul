def Login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def ShowWelcomeMenu():
    print("Access completed!")
    print("Welcome to Pongpeng Shop")
    print("----------------------------------")
    print("Please select which program you want to access")
    print("1. Price(1 product) calculator")
    print("2. Price(more than 1 product) calculator")
def SelectProgram():
    userSelected = int(input("Select program :"))
    return userSelected
def Price1prodCal(TotalPrice):
    vat = 7
    result = TotalPrice + (TotalPrice * vat / 100)
    return result
def PriceMorethan1prodCal():
    price1 = int(input("Price for product1 :"))
    price2 = int(input("Price for product2 :"))
    return Price1prodCal(price1+price2)


if  Login() == True:
    ShowWelcomeMenu()
    userselected = SelectProgram()
    if userselected == 1:
        TotalPrice = int(input("Enter Price(Only 1): "))
        print("The Total Price will be ", Price1prodCal(TotalPrice), "THB")
    elif userselected == 2:
        print("The Total Price will be ", PriceMorethan1prodCal(), "THB")
    else:
        print("Wrong selection")


else:
    print("Access Denied")





