def vatCalculator(Price):
    TotalPrice = Price+(Price*7/100)
    return TotalPrice

print(vatCalculator(int(input("Please Enter price of the product :"))))

