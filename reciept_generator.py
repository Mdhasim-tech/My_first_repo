# reciept generator program
#my code
'''while True:
    print("input the prices of the items in space seperated values below----")

    lst=list(map(int,input().split()))
    print("the sum of the prices of items are",sum(lst))'''

#harry"s code
sum = 0
while True:
    userinput = input("Enter the item price or press q to quit:\n")
    if userinput != "q":
        sum = sum + int(userinput)
        print(f"order total so far: {sum}")
    else:
        print(f"your bill total is {sum}.Thanks for shopping with us")
        break
