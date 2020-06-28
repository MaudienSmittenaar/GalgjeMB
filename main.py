import re
import random
import time

counter = 0
woordenlijst = ["school", "corona", "leerwerk", "huiswerk", "vakantie", "zomer", "python","informatica", "winnaar", "computer", "schoolboek", "zon", "zwemmen", "uitrusten"]

hetwoord = random.choice(woordenlijst)
lengtewoord = len(hetwoord)
temp = "." * lengtewoord

print("We spelen het spel galgje. Leuk dat je meedoet!")   
print("Raad letters en kom zo achter het woord. Weet het je hele woord? Type dan het woord voluit om te winnen!")

time.sleep(5)

print()
print("Intotaal het je 10 levens. Bij de 10de keer dat je een foute letter hebt gekozen of het foute woord aangeeft, ben je dood.")

time.sleep(5)
print()
print("Laten we beginnen!")
print()
print("Om je een beetje opweg te helpen vertel ik je hoeveel letters het woord heeft!")
print("Het woord heeft " + str(lengtewoord) + " letters") 

while True:
  gokje = (input(": "))
  match = re.search(gokje, hetwoord)
  if gokje == hetwoord: 
    print('Goed gedaan! Je heb het woord ' + '"' + hetwoord + '"' + " geraden")
    break
  
  elif match: 
    print("Goed geraden! Ga zo door.")
    for i in range(0, lengtewoord):
      if gokje == hetwoord[i]:
        temp = temp[:i] + gokje +temp[i+1:]
    print(temp)

  else: 
    print("Nee helaas! Deze letter zit niet in het woord.")
    counter = counter + 1
    if counter == 1:
      print("""  
     |
     |
     |
     |
     |
_____|""")
    elif counter == 2:
      print("""____
     |
     |
     |
     |
     |
_____|""")
    elif counter == 3:
            print("""  ____
    \|
     |
     |
     |
     |
_____|""")
    elif counter == 4:
      print("""  ____
  | \|
     |
     |
     |
     |
_____|""")
    elif counter == 5:
      print("""  ____
  | \|
  0  |
     |
     |
     |
_____|""")
    elif counter == 6:
      print("""  ____
  | \|
  0  |
  |  |
     |
     |
_____|""")
    elif counter == 7:
      print("""  ____
  | \|
  0  |
 /|  |
     |
     |
_____|""")
    elif counter == 8:
      print("""  ____
  | \|
  0  |
 /|\ |
     |
     |
_____|""")
    elif counter == 9:
      print("""  ____
  | \|
  0  |
 -|- |
 /   |
     |
_____|""")
    elif counter == 10:
      print("""  ____
  | \|
  0  |
 -|- |
 / \ |
     |
_____|""") 
      time.sleep(0.5)
      print('Jammer! Je hebt het woord niet weten te raden. Speel opnieuw en win!')
      break 