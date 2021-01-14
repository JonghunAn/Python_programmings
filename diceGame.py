import easygui,random

com = random.randint(1,18)
user = 0
chance = 3

name = easygui.enterbox("Write your name")
easygui.buttonbox("Play rolling a dice",choices=["Roll"])

while chance>=0:
    if chance>1 :
        chance-=1
        value = random.randint(1,6)
        user += value
        easygui.buttonbox("You got "+str(value)+"\n"+str(chance)+" times left",choices=["Roll"])
    else:
         value = random.randint(1,6)
         user += value
         easygui.buttonbox("You got "+str(value)+"\nNo more chance..",choices=["Show the result"])
         break

if(com<user) :
    result = "You Win!"
elif(com==user):
    result = "Draw!"
elif(com>user): 
    result = "You lose..."

easygui.msgbox(name+"'s Final Score : "+str(user)+"\nComputer score : "+str(com)+"\n"+result)
