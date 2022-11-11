import random
import pyttsx3 as pt

def scissors_game():   
    player=0
    cpu=0
    engine=pt.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say("welcome to rock paper scissors game ")
    engine.runAndWait()

    while player<3 and cpu<3:
        cpu_choice=random.choice(["rock","paper","scissors"])

        player_choice=input("rock,paper,scissors : ")

        print("cpu:",cpu_choice,"player:",player_choice)

        if player_choice==cpu_choice:
            engine.say("tie! no points")
            engine.runAndWait()
  
        elif player_choice.lower()=="rock":
            if cpu_choice.lower()=="scissors":
                player+=1
                engine.say(f"player wins {player} games")
                engine.runAndWait()
            elif cpu_choice.lower()=="paper":
                cpu+=1
                engine.say(f"cpu wins {cpu} games")
                engine.runAndWait()

        elif player_choice.lower()=="scissors":
            if cpu_choice.lower()=="paper":
                player+=1
                engine.say(f"player wins {player} games")
                engine.runAndWait()
            elif cpu_choice.lower()=="rock":
                cpu+=1
                engine.say(f"cpu wins {cpu} games")
                engine.runAndWait()

        elif player_choice.lower()=="paper":
            if cpu_choice.lower()=="rock":
                player+=1
                engine.say(f"player wins {player} games")
                engine.runAndWait()
            elif cpu_choice.lower()=="scissors":
                cpu+=1
                engine.say(f"cpu wins {cpu} games")
                engine.runAndWait()

        else:
            engine.say("invalid input")  
            engine.runAndWait()
 
    if player==3:
        engine.say("the total game won by player")
        engine.runAndWait()
    else:
        engine.say("the total game won by cpu")
        engine.runAndWait()
        
    return None    


scissors_game()