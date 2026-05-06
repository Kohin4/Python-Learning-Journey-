num = int(input("Give a integer number : "))
temp = False
i = 2
root = num**0.5
while i<=root:
    if num%i==0:
        print("Not Prime")
        temp = True
        break
    i +=1    
if temp==False:
    print("Prime")
