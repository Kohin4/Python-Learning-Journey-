def clean(n):
    return int(n) if n.is_integer() else round(n,15)

print("Hello Sir,Please select the operation what you wanna do")
print("=======================================================")

counter = 0

while True:
    
    print("\n\n0.Exit")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power")    
    
    try:
        h = int(input("Choose an option : "))
    except ValueError:
        print("Invalid Input,Try Again")
        continue
       
    if h==0:
        break
        
    elif h<1 or h>5:
        print("Invalid Input,Try Again")
        continue
        
    num1=float(input("Please Give the 1st Number : "))
    num2=float(input("Please Give the 2nd Number : "))
    
    if h==1:
        print(f"{clean(num1)} + {clean(num2)} = {clean(num1+num2)}")
        counter += 1
        
    elif h==2:
        print(f"{clean(num1)} - {clean(num2)} = {clean(num1-num2)}")
        counter += 1
        
    elif h==3:
        print(f"{clean(num1)} × {clean(num2)} = {clean(num1*num2)}")
        counter += 1 
        
    elif h==4:
        
        if num2==0:
            print(f"{clean(num1)} ÷ 0 = Infinity")
            counter += 1
            
        else:    
            print(f"{clean(num1)} ÷ {clean(num2)} = {clean(num1/num2)}")
            counter += 1 
        
    elif h==5:
        print(f"{clean(num1)} ^ {clean(num2)} = {clean(num1**num2)}")
        counter += 1
        
        
print("Thanks for Using me Sir")
print("You did total",counter,"operations")      
