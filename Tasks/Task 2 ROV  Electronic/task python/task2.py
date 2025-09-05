def add (num1, num2):
    print (num1+num2)
def mui(num1,num2):
    print(num1-num2)
def mal(num1,num2):
    print (num1*num2)
def div (num1,num2):
    print(num1/num2)
while(True):
    int(num1=input("enter number 1"))
    int(num2=input("enter number 2"))
    op=input("choose (+,-,*,/)")
    if op=='+':
        add (num1,num2)
    elif op=='-':
        mui(num1,num2)
    elif op=='*':
        mal(num1,num2)
    elif op=='/':
        div(num1,num2)