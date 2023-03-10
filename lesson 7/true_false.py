def sum(num, answ, rest):
    f = []
    for item in num:
        f.append(float(item))
    answ = int(answ)
    rest = int(rest)
    sum_n = 0
    for i in range(len(f)):
        sum_n = sum_n + float(f[i])
    if sum_n/len(f) == answ and sum_n%len(f) == rest:
        return True
    else:
        return False


# file = open("numbers.txt", "r")
# numb = []
# for x in file:
#     numb, answ, rest = x.split(";")


numb = [2, 4, 5]
answ = 3
rest = 2


print(sum(numb,answ,rest))

