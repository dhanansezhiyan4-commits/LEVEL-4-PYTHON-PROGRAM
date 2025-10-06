print("Fibonacci Serices")
print("-----------------")
n=int(input("Enter the Number:"))
print("Fibonacci Serices")
a=-1
b=1
for i in range(n+1):
    c=a+b
    print(c)
    a=b
    b=c
