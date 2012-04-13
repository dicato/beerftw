import csv
from beerswap.models import Beer, Person

reader = csv.reader(open('beer.csv', 'rb'))

for row in reader:
    pname = row[0].strip()
    name = row[1].strip()
    brewery = row[2].strip()
    rating = int(row[3].strip())

    person = Person.objects.get(name=pname)
    b = Beer(person = person, name = name, brewery = brewery, rating = rating)
    b.save()
    
