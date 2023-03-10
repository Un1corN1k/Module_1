print("Enter your age: ")
Age = int(input())
print(f"Hello,I'm {Age} year's old!")
if Age >= 21:
    print("Hi, man!")
elif 21 > Age >= 18:
    print("Hi, adult!")
elif 18 > Age > 7:
    print("Hi, kid!")
else:
    print("Hi, baby!")
