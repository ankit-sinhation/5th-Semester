import random

jackpot=random.randint(1,100)
print("Guess the jackpot no between 1 to 100.")
#print("the jackpot number is" ,jackpot)

counter=1

guess=input("Guess kar bro : ")
while guess!=jackpot:
    try:
        guess=float(guess)
        if(guess==jackpot):
            exit
        elif(guess<jackpot):
            print("Galat hai bro, guess higher : ")
        else:
            print("Galat hai bro, guess lower : ")

    except:
        if(guess=="i am sumit"):
            print("try to guess digits, example:",100-jackpot)
        else:
            print("try to guess digits, example:",random.randint(1,100))
    if(guess!=jackpot):
        guess=input("Firse guess kar : ")
        counter = counter+1

    
print(counter-1,"br kosis krne k baad jaa kr..")
print(jackpot,"hai sahi jawab !!!")
