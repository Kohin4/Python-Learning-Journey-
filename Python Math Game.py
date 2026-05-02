import random

def make_integer(n):
    return int(n) if n.is_integer() else n


score = 0

print("Hello Sir,Welcome to The Game")
print("*****************************\n")

while True:
    
    print("=================================================")
    permission = input("\nContinue - #\nExit - *\nYour Command : ")
    
    print("\n")
    
    if permission == "*":
        print("Thanks For Playing The Game")
        break;
        
    elif permission == "#":
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        sign = random.choice(["+","-","×","÷"])
        print(f"{num1} {sign} {num2} =",end=" ")
        
        try:
            user_input = float(input())
        except ValueError:
            print("Invalid Input\nScore : -1")
            score -= 1   
            continue
        
        
        user_input = make_integer(user_input)   
         
        if sign=="+":
            if user_input == num1+num2:
                print("Right, Score : +1")
                score += 1
            else:
                print("Wrong, Score : -1")
                score -= 1    
        
        elif sign=="-":
            if user_input == num1-num2:
                print("Right, Score : +1")
                score += 1
            else:
                print("Wrong, Score : -1")
                score -= 1 
                
        elif sign=="×":
            if user_input == num1*num2:
                print("Right, Score : +1")
                score += 1
            else:
                print("Wrong, Score : -1")
                score -= 1 
        
        elif sign=="÷":
            if abs(user_input-(num1/num2))<0.01:
                print("Right, Score : +1")
                score += 1
            else:
                print("Wrong, Score : -1")
                score -= 1
    
    else:
        print("Invalid Command,Try Again")     
               
print("Your Score : ",score)
