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


print('Enter the value of the fizz variable: ')
fizz = int(input())
print('Enter the value of the buzz variable: ')
buzz = int(input())
print('Enter the string length: ')
n = int(input())
print(f'Here is your result: {Fizz_Buzz(fizz,buzz,n)}')
