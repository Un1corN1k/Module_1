def Fizz_Buzz(fizz, buzz, n):
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
    return f'Here is your result: {result}'

fizz = int(input('Enter the value of the fizz variable: '))
buzz = int(input('Enter the value of the buzz variable: '))
n = int(input('Enter the string length: '))
print(Fizz_Buzz(fizz, buzz, n))