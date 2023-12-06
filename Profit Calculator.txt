made = float(input("How much gross money did you make? $"))
lost = float(input("How much gross money did you lose? $"))
taxrate = float(input("What percentage were you taxed? (In decimal form) "))
if taxrate == 0:
    netprofit = made - lost
else:
    netprofit = made - lost
    if taxrate < 1:
        netprofit *= taxrate
    else:
        netprofit /= taxrate
rounded_profit = round(netprofit, 2)
if rounded_profit > 0:
    print(f"You made ${rounded_profit}.")
elif rounded_profit < 0:
    print(f"You lost ${-rounded_profit}.")
else:
    print(f"You made no profit, nor did you lose money.")
