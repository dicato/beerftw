import csv
from beerswap.models import Beer, Person

nameFile = open('names.txt')
for n in nameFile.readlines():
    p = Person(name=n.strip())
    p.save()
    