print("Stock price = 30/-.")
print("Lock price = 45/-.")
print("Barrel price = 25/-.")
stocks = int(input("Enter the number of stocks:"))
barrels = int(input("Enter the number of barrels:"))
locks = int(input("Enter the number of locks:"))
if stocks<1 or stocks>80:
    print("Stocks out of range(1 and 80).")
    exit()
if barrels<1 or barrels>90:
    print("Barrels out of range(1 and 90).")
    exit()
if locks<1 or locks>70:
    print("Locks out of range(1 and 70).")
    exit()
sales = stocks*30 + locks*45 + barrels*25
if sales<=1000:
    commission = sales*0.1
elif sales>1000 and sales<=1800:
    commission = sales*0.15
else:
    commission = sales*0.2
print("Grand total: ",sales)
print("Commission given: ",commission)

