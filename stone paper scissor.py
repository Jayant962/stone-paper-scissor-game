import random
l=["Rock","Paper","Scissor"]
'''
rock vs paper->paper wins
rock vs scissor->rock wins
paper vs scissor->scissor wins
'''
while True:
    ucount=0
    ccount=0
    uc=int(input('''
Game Start....
1. Play
2. Exit
    '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1. Rock
2. Paper
3. Scissor
'''))
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice="Paper"
            elif userinput==3:
                uchoice="Scissor"
            else:
                print("invalid input")
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("Computer choice:",cchoice)
                print("User choice:",uchoice)
                print("Game Draw")
            elif (cchoice=="Rock" and uchoice=="Paper") or (cchoice=="Paper" and uchoice=="Scissor") or (cchoice=="Scissor" and uchoice=="Rock"):
                print("Computer choice:", cchoice)
                print("User choice:", uchoice)
                print("You Win")
                ucount+=1
            else:
                print("Computer choice:", cchoice)
                print("User choice:", uchoice)
                print("Computer Win")
                ccount+= 1
        if ucount==ccount:
                print("Final Game Draw...")
                print("Your Point:",ucount)
                print("Computer Point:",ccount)
        elif ucount>ccount:
                print("Your Point:", ucount)
                print("Computer Point:", ccount)
                print("Final You Win...")
        else:
                print("Final Computer Win...")
                print("Your Point:", ucount)
                print("Computer Point:", ccount)
    else:
        break