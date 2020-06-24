import re
import random

woordenlijst = ["school", "corona", "leerwerk", "huiswerk", "vakantie", "zomer", "python","informatica", "winnaar", "computer", "schoolboek", "zon", "zwemmen", "uitrusten"]

hetwoord = random.choice(woordenlijst)
lengtewoord = len(hetwoord)
temp = "." * lengtewoord

print("We spelen het spel galgje. Leuk dat je meedoet! Raad letters en kom zo achter het woord. Weet het je hele woord? Type dan het woord voluit om te winnen! Laten we beginnen! Om je een beetje opweg te helpen vertel ik je hoeveel letters het woord heeft. Het woord heeft " + str(lengtewoord) + " letters") 

