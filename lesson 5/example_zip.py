print("Enter the names of the participants: ")
name =list(map(str, input().split()))
print("Enter their work experience: ")
age = list(map(int, input().split()))
print("Enter their gender: ")
gender = list(map(str, input().split()))


def _zip_(name,age,gender):
    return zip(name,age,gender)

print(f'Here is your sorted member list: {list(_zip_(name, age, gender))}')
