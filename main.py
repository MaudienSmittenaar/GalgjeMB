import re
import random

counter = 0
woordenlijst = ["school", "corona", "leerwerk", "huiswerk", "vakantie", "zomer", "python","informatica", "winnaar", "computer", "schoolboek", "zon", "zwemmen", "uitrusten"]

hetwoord = random.choice(woordenlijst)
lengtewoord = len(hetwoord)
temp = "." * lengtewoord

print("We spelen het spel galgje. Leuk dat je meedoet! Raad letters en kom zo achter het woord. Weet het je hele woord? Type dan het woord voluit om te winnen! Laten we beginnen!")
print("Om je een beetje opweg te helpen vertel ik je hoeveel letters het woord heeft!")
print("Het woord heeft " + str(lengtewoord) + " letters") 

while True:
  gokje = (input(": "))
  match = re.search(gokje, hetwoord)
  if gokje == hetwoord: 
    print('Goed gedaan! Je heb het woord ' + '"' + hetwoord + '"' + " geraden")
    break
  
  elif match: #goed geraden letter
    print("Goed geraden! Ga zo door.")
    for i in range(0, lengtewoord):
      if gokje == hetwoord[i]:
        temp = temp[:i] + gokje +temp[i+1:]
    print(temp)