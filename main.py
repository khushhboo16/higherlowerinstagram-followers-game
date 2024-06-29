import art
import game_data
from art import logo,vs
from game_data import data
print(logo)

import random
def compare(A,B):
  if A['follower_count']> B['follower_count']:
    return A
  else:
    return B
def game():
  flag= True
  score=0
  A=random.choice(data)
  B= random.choice(data)
  while flag==True:  
   A=B
   B=random.choice(data) 
   if B==A:
     B=random.choice(data)
     
   print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
   print(vs)
   print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}")
   user_input=input("Who do you think has more followers? Type A or B: ")
   if user_input=="A" and compare(A,B)==A:
     score+=1
     print(f"YOU ARE CORRECT AND YOUR SCORE IS {score}")
     
     flag= True
   elif user_input =="B" and compare(A,B)==B:
     
     
     score+=1
     print(f"YOU ARE CORRECT AND YOUR SCORE IS {score}")
     flag= True
   else:
     print(f"YOU ARE WRONG AND YOUR SCORE IS {score}")
     flag= False
     
game()   
  
 
  