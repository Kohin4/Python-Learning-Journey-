import random
print("★★★ Hello,Welcome to the ROCK,PAPER,SCISSORS Game ★★★")
while True:
    
    pro_value = random.randint(1,3)
    print("\n\n=====================================================")
    print("\n√√√√√√√√√√√√ I Took My Turn √√√√√√√√√√√√")
    print("\n!!!!!!!!! Now Your Turn !!!!!!!!!")
    print("\t  1.Rock")
    print("\t  2.Paper")
    print("\t  3.Scissor")
    
    try:
        my_value = int(input("\nChoose one of these : "))
    except ValueError:
        print("\nInvalid Input,Try again")
        continue    
    
    if my_value>=1 and my_value<=3:
        print("-------------------------------------")
    
        print("\n\tMy Choice   :",end=' ')
    
        if pro_value == 1:
            print("Rock")
        elif pro_value==2:
            print("Paper")    
        else:
            print("Scissor")    
        
    
        print("\tYour Choice :",end=' ')
    
        if my_value == 1:
            print("Rock")
        elif my_value==2:
            print("Paper")    
        else:
            print("Scissor")
        print("\n-------------------------------------")
    
        if my_value == pro_value:
            print("\n\tIts Draw")
            print("\tLet's try again")
     
        elif my_value==1 and pro_value == 2:
            print("\n\tYou Lost")
            print("\tLet's try again")
        
        elif my_value==2 and pro_value == 3:
            print("\n\tYou Lost")
            print("\tLet's try again") 
        
        elif my_value==3 and pro_value == 1:
            print("\n\tYou Lost")
            print("\tLet's try again")    
   
        else:
            print("\n=================== You are Winner ==================")
            print("\n------------ Thanks for Playing the Game ------------")
            print("\n>>>>>>>>Open the Program again for play again<<<<<<<<")
            break
    
    else:
        print("\nInput should be between 1 and 3,Try Again")   
