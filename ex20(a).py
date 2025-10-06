print("Prime Number Checking")
print("---------------------")
n=int(input("Enter the Number:"))
print("Result:")
count=0
for i in range(2,n):
    if(n%i==0):
        count=count+1
    if count==0:
         print(n,"is Prime")
    else:
         print(n,"is a not Prime")                                                                                                                                                                    
