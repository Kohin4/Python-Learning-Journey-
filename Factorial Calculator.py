num = int(input("Give an integer number : "))
if num==0:
    print(1)
    
else:
    i = 2
    ans = 1
    while i<=num:
        ans = i*ans
        i += 1
    print(ans)          
