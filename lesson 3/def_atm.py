def atm_100(value):
    rest = value
    nominal_10 = 0
    
    while rest >= 10:
        rest = rest - 10
        if rest >= 0 and nominal_10 < 10:
            nominal_10 = nominal_10 + 1
        else:
            rest = rest + 10
    return f"Here's your money: 10 x {nominal_10}"


def atm_300(value):
    rest = value
    nominal_20 = 0
    nominal_10 = 0

    while rest >= 20:
        rest = rest - 20
        if rest >= 0 and nominal_20 < 10:
            nominal_20 += 1
        else:
            rest = rest + 20
            break
        while rest <= 10 * 10:
            while rest >= 10:
                rest = rest - 10
                if rest >= 0 and nominal_10 < 10:
                    nominal_10 += 1
                else:
                    rest = rest + 10
            return f"Here's your money: 20 x {nominal_20} and 10 x {nominal_10}"


def atm_1000(value):
    rest = value
    nominal_50 = 0
    nominal_20 = 0
    nominal_10 = 0

    while rest >= 50:
        rest = rest - 50
        if rest >= 0:
            nominal_50 = nominal_50 + 1
        else:
            rest = rest + 50
            break
        while rest <= (20 * 10) + (10 * 10):
            while rest >= 20:
                rest = rest - 20
                if rest >= 0 and nominal_20 < 10:
                    nominal_20 += 1
                else:
                    rest = rest + 20
                    break
                while rest <= 10 * 10:
                    while rest >= 10:
                        rest = rest - 10
                        if rest >= 0 and nominal_10 < 10:
                            nominal_10 += 1
                        else:
                            rest = rest + 10
                    return f"Here's your money: 50 x {nominal_50} and 20 x {nominal_20} and 10 x {nominal_10}"


print("Enter the amount of money to exchange:")
x = int(input())


if x <= 100:
    print(atm_100(x))
elif 100 < x <= 300:
    print(atm_300(x))
else:
    print(atm_1000(x))
