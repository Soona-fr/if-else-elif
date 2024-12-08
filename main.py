first = int(input('Enter your first number: '))
second = int(input('Enter your second number: '))
third = int(input('Enter your third number: '))
#-----------------------------------------
if first == second and first == third:
    print(3)
elif first == second or first == third:
    print(2)
elif second == third:
    print(2)
else:
    print(0)