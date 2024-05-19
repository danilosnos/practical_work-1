max=int(input("Введите максимальное число:"))
if max<1:
    print("Максимальное число должно быть не меньше 1")
else:
 for i in range(1,int(max+1)):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)