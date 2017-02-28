# camelgame
#camel game!
import random
print("Welcome to Camel!")
print("You have stolen a Camel to make your way across the great Mobi Desert.")
print("The natives want their camel back and they're gonna kill you if they find you")
print("Survive the journey and outrun the natives.")
done=bool
done = false
you=0
you=int(you)
natives=-20
natives=int(natives)
camel=100
camel=int(camel)
thirst=100
thirst=int(thirst)
if you >= 200:
    done=true
    print("You have won the game! You have made it out of the desert! Congrats!")
if natives >= you:
    print("The natives have caught up to you, and you are DEAD.")
    done = true
if camel == 0:
    print("Your camel has fallen over and died. You die of heatstroke in the desert.")
    done=true
if thirst == 0:
    print("You have DIED of dehydration. Better luck next time!")
    done=true
while done == false:
    print("The desert seems endless, what will you do?")
    print("A. Ride at full speed")
    print("B. Drink some water")
    print("C. Rest")
    print("D. Ride at a steady speed")
    print("E. Check your camel and thirst, and use your GPS")
    choice=input('Your choice: ')
    if choice == "A" or choice == "a":
        print("You ride 25 miles. Your camel lost energy, you're slightly more thirsty.")
        you=you+25
        natives=natives+23
        camel=camel-20
        thirst=thirst-20
        
    elif choice == "b" or choice == "B":
        print("You drank water, your thirst goes down but the natives are getting closer.")
        you=you+5
        natives=natives+23
        camel=camel+5
        thirst=thirst+20
    elif choice == "c" or choice == "C":
        print("You and your camel got some rest, but the natives are getting closer.")
        you=you+1
        natives=natives+23
        camel=camel+25
        thirst=thirst-3
    elif choice == "d" or choice == "D":
        print("You ride 15 miles, but you get more thirsty, and your camel loses energy.")
        you=you+15
        natives=natives+23
        camel=camel-15
        thirst=thirst-20
    elif choice == "e" or choice == "E":
        print("You are ", you ," miles out of 200 miles.")
        print("The natives are ", you-natives , "miles away from you")
        print("The camel has ", camel ,"energy out of 100."
        print("You are ", thirst, "thirst out of 100.")
