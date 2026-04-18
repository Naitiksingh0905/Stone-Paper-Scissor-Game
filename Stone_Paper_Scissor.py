'''
1 as Stone
-1 as Paper
0 as Scissor


'''
import random

computer=random.choice([-1, 1, 0])
youstr=str(input("Stone | Paper | Scissor\nEnter your choice:"))
youDict={'Stone':1, 'Paper':-1, 'Scissor':0}
reverseDict={1:'Stone', -1:'Paper', 0:'Scissor'}
younum=youDict[youstr]

print(f"Computer choose {reverseDict[computer]}.")
print(f"You choosed {youstr}.")

if computer == younum:
    print("Draw.")
elif (computer==1 and younum==-1):
    print("You win!")
elif (computer==1 and younum==-0):
    print("You lose! Try again.")
elif (computer==-1 and younum==1):
    print("You win!")
elif (computer==-1 and younum==0):
    print("You win!")
elif (computer==0 and younum==1):
    print("You win!")
elif (computer==0 and younum==-1):
    print("You lose! Try again.")

else:
    print("Something went wrong!!!")