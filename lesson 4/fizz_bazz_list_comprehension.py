def Fizz_Buzz(f: int, b: int, n: int):
    r = []
    range_number = [*range(1, n+1)]

    # fizz = [ i for i in range_number if i % f == 0]
    # bazz = [ i for i in range_number if i % b == 0]
    # fizz_bazz = [ i for i in range_number if i % b == 0 and i % f == 0]

    result = ["FB" if (i % f == 0 and i % b == 0) else "F" if (i % f == 0) else "B" if (i % b == 0)
    else i for i in range_number]

    return result

print('Enter the value of the fizz variable: ')
f = int(input())
print('Enter the value of the buzz variable: ')
b = int(input())
print('Enter the string length: ')
n = int(input())
print(f'Here is your result: {Fizz_Buzz(f,b,n)}')