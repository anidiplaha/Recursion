def isEven(num):
     if(num<2):
         return (num%2 == 0)
     return (isEven(num-2))
num=int(input("Enter the number for check odd or even: "))
if(isEven(num)==True):
    print(num,"is an even number")
else:
    print(num,"is an odd number")