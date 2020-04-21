def vatCalculator():
    Price = int(input("Enter Price of the product :"))
    TotalPrice = Price+(Price*7/100)
    print("The Total Price will be ", TotalPrice, "THB")
vatCalculator()
