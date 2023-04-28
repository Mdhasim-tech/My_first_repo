import math
import functools as f
print("use the calculator as per your convenience time.Enter q to exit")
while True:
    inp = input('which operation do you want to perform? \n add + ,subtract -  ,multiply * ,divide / ,floor division //,factorial !,square (sq),square root (sqrt),modulus %:', )

    if inp == '+' or inp=="add":
        print("Enter the numbers below---")
        lst = list(map(int, input().split()))
        addd = f.reduce(lambda a, b: a + b, lst)
        print('the sum is', addd)



    elif inp == "factorial" or inp=="!":
        print("Enter the number below---")
        def factorial_recursive(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial_recursive(n-1)
        n=int(input())
        print(factorial_recursive(n))



    elif inp=="-" or inp=="subtract":
        print("Enter the numbers below---")
        lst = list(map(int, input().split()))
        sub=f.reduce(lambda a,b:a-b,lst)
        print("the subtracted value is",sub)



    elif inp=="*" or inp=="multiply":
        print("Enter the numbers below---")
        lst=list(map(int,input().split()))
        mul=f.reduce(lambda a,b:a*b,lst)
        print(mul)


    elif inp=="/" or inp=="divide":
        print("Enter the numbers below---")
        lst=list(map(int,input().split()))
        div=f.reduce(lambda a,b:a/b,lst)
        print(div)


    elif inp=="//" or inp=="floor division":
        print("Enter the two numbers below---")
        def floor_division(a,b):
            return a//b
        a,b=map(int,input().split())
        fd=floor_division(a,b)
        print(fd)

    elif inp=="square" or inp=="sq":
        print("Enter first number as the base and the second number as the power---")
        a,b=map(int,input().split())
        sqr=lambda a,b:a**b
        print(sqr(a,b))

    elif inp=="square root" or inp=="sqrt":
        print("Enter the number below---")
        a=int(input())
        print(math.sqrt(a))

    elif inp=="modulus" or inp=="%":
        print("Enter the two numbers below---")
        a,b=map(int,input().split())
        print(a%b)

    else:

        print("Thanks for using me!!")
        break