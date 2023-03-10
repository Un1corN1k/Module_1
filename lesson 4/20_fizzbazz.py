def Fizz_Buzz(fizz: int, buzz: int, n: int):
    result = " "
    for fizzbuzz in range(1, n + 1):
        if fizzbuzz % fizz == 0 and fizzbuzz % buzz == 0:
            result += 'FB' + ' '
        elif fizzbuzz % fizz == 0:
            result += 'F' + ' '
        elif fizzbuzz % buzz == 0:
            result += 'B' + ' '
        else:
            result += str(fizzbuzz) + ' '
    return result


file = open("../lesson 7/data.txt", "r")
file_2 = open("data2.txt", "w")


for x in file:
    fizz, buzz, n = x.split()
    file_2.write(Fizz_Buzz(int(fizz), int(buzz), int(n)))
    file_2.write("\n")


file.close()
file_2.close()





