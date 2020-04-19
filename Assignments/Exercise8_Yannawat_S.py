usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput =="password":
    print("-------------------------------")
    print("    Welcome to pizza company   ")
    print("-------------------------------")
    print("Please select the pizzas by typing the number")
    print("Example: If you select Super deluxe pizza, Type 2")
    print("1. Hawaiian          350 THB")
    print("2. Super deluxe      450 THB")
    print("3. Cocktail Seafood  510 THB")
    PizzaSelect = int(input("Select pizza number :"))
    if PizzaSelect == 1:
        print("How many Hawaiian pizza do you want?")
        AmountHawaiian = int(input("Please enter: "))
        print("--------------------------------------------------")
        Total = (AmountHawaiian * 350)

    elif PizzaSelect == 2:
        print("How many Super deluxe pizza do you want?")
        AmountSuper = int(input("Please enter: "))
        print("--------------------------------------------------")
        Total = (AmountSuper * 450)

    elif PizzaSelect == 3:
        print("How many Cocktail Seafood pizza do you want?")
        AmountCocktail = int(input("Please enter: "))
        print("--------------------------------------------------")
        Total = (AmountCocktail * 510)
    else:
        print("There is no pizza for this number")
        Total =0
    print("  Total Price will be", Total, "THB")
    MoreOrder = input("Order more?(Y/N) :")
    if MoreOrder == "Y":
        print("1. Hawaiian          350 THB")
        print("2. Super deluxe      450 THB")
        print("3. Cocktail Seafood  510 THB")
        MoreOrderPizzaSelect = int(input("Select pizza number :"))
        if MoreOrderPizzaSelect == 1:
            print("How many Hawaiian pizza do you want?")
            AmountHawaiian2 = int(input("Please enter: "))
            Total2 = (AmountHawaiian2 * 350)
            print("The total price will be :", Total+Total2, "THB")
        elif MoreOrderPizzaSelect == 2:
            print("How many Super deluxe pizza do you want?")
            AmountSuper2 = int(input("Please enter: "))
            Total2 = (AmountSuper2 * 450)
            print("The total price will be :", Total + Total2, "THB")
        elif MoreOrderPizzaSelect == 3:
            print("How many Hawaiian pizza do you want?")
            AmountCocktail2 = int(input("Please enter: "))
            Total2 = (AmountCocktail2 * 510)
            print("The total price will be :", Total + Total2, "THB")
        else:
                print("There is no pizza for this number")
    elif MoreOrder == "N":
        print("Thank you for ordering us!!")
        print("The total price will be :", Total, "THB")
    else:
        print("What did u just type? Please type Y=Yes, N=No")

else:
    print("You need to pay more attention. Try Again!!! ")




