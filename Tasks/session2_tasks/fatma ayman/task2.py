def stars():
    n = int(input("enter a number between 1 and 20  "))

    if n <1 or n>20:
        print("please enter a number between 1 and 20")
        return

    for i in range(1,n+1):
           print("*" * i)


stars()