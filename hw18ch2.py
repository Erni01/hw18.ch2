# 18. Write the code, which will print numbers from 0 till your age.
# And if your age is odd, will be printed all odd numbers till your age, if even all even numbers.

age = int(input("Enter Your age: "))

for i in range(age + 1):
    if age % 2 == 0:
        if i % 2 == 0:
            print(i)
    if age % 2 == 1:
        if i % 2 == 1:
            print(i)