n = int(input("Enter the number of input : "))
i= 1
while i<=n:
    num = int(input())
    if i == 1:
        Maximum = num
    else:
        Maximum = max(num,Maximum)
    i += 1    
print("Maximum Number is : ",Maximum)        
    
