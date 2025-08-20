print("Sum of n Number")
print("---------------")
a=int(input("Enter the Starting Number:"))
b=int(input("Enter the Ending Number:"))
print("Result")
print("------")
print("Series")
count=0
sum=0
for i in range(a,b+1):
    if(i%5==0)and(i%3==0):
        print("+",+i)
        sum=sum+i
        count=count+1
        print("Sum Values:",sum)
        print("Count Values:",count)
