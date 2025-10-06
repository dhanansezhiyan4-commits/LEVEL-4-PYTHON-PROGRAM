print("Prime Number Cheching")
print("---------------------")
sn=int(input("Enter the Starting Number:"))
en=int(input("Enter the Ending Number:"))
print("Result")
for n in range(sn,en+1):
    if n < 2:
        print(n,"Not Prime")
        continue
    count=0
    for i in range(2,n):
        if n %i==0:
            count+=1
            break
    if count==0:
        print(n,"Prime")
    else:
        print(n,"Not Prime")
