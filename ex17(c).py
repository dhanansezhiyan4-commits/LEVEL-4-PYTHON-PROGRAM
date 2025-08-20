print("Sum of n Number")
print("---------------")
a=int(input("Enter the Starting Number:"))
b=int(input("Enter the Ending Number:"))
c=int(input("Enter the Different:"))
print("Result=")
print("-------")
print("Series")
count=0
sum=0
for i in range(a,b+1,c):
    print("+",+i)
    sum=sum+i
    count=count+1
    print("sum",sum)
    print("sum values:",sum)
    print("count value:",count)
