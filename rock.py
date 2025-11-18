
import random
user_choice=int(input("Enter your choice: type 0 for Rock,type 1 for paper,type 2 for scissor"))
computer_choice=random.randint(0,2)
print("computer choose:",computer_choice)
if computer_choice== user_choice:
    print("Its a draw")
elif computer_choice == 0 and user_choice ==2:
     print("you loose")
elif computer_choice == 2 and user_choice ==0:
     print("you win")
elif computer_choice > user_choice:
     print("tou loose")
elif user_choice > computer_choice:
     print("you win") 
