def atm(value):
    rest = value
    result = ""
    nominal_500 = 0
    nominal_100 = 0
    nominal_50 = 0
    nominal_20 = 0
    nominal_10 = 0
    if rest - 500 >= 0:
        while True:
            rest = rest - 500
            if rest >= 0:
                nominal_500 = nominal_500 + 1
            else:
                rest = rest + 500
                break
    if rest - 100 >= 0:
        while True:
             rest = rest - 100
             if rest >= 0:
                 nominal_100 = nominal_100 + 1
             else:
                 rest = rest + 100
                 break
    if rest - 50 >= 0:
        while True:
            rest = rest - 50
            if rest >= 0:
                nominal_50 = nominal_50 + 1
            else:
                rest = rest + 50
                break
    if rest - 20 >= 0:
        while True:
             rest = rest - 20
             if rest >= 0:
                 nominal_20 = nominal_20+1
             else:
                 rest = rest + 20
                 break
    if rest - 10 >= 0:
         while True:
            rest = rest - 10
            if rest >= 0:
                nominal_10 = nominal_10+1
            else:
                rest = rest + 10
                break
    result = "Here's your money:"+ " " + "500 x " + str(nominal_500) + "; " + "100 x " + str(nominal_100) + "; " + "50 x " + str(nominal_50) + "; "+ "20 x " + str(nominal_20) + "; " + "10 x"+ str(nominal_10)
    return result


print("Enter the amount of money to exchange:")
x = int(input())
print (atm(x))