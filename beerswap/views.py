import operator
from django.http import Http404
from django.template import Context, loader
from beerswap.models import Person, Beer
from django.http import HttpResponse
from django.shortcuts import render_to_response

def beers(request):
    all = Beer.objects.all()
    return render_to_response('beerswap/beers.html', {'beers': all})

def beer_detail(request, beer_id):
    try:
        b = Beer.objects.get(pk = beer_id)

    except Beer.DoesNotExist:
        raise Http404

    return render_to_response('beerswap/beer.html', {'beer': b})
    
def people(request):
    all = Person.objects.all()
    return render_to_response('beerswap/people.html', {'people': all})

def person_detail(request, person_id):
    try:
        p = Person.objects.get(pk = person_id)

    except Person.DoesNotExist:
        raise Http404

    beers = Beer.objects.filter(person__id = p.id)
    return render_to_response('beerswap/person.html', {'person': p, 'beers': beers})

def leaderboard(request):
    meta = {'first':'Grand Brewmeister',
              'second':'King of the Growlers',
              'third':'Prince of the Pint',
              'middle':'Common pint drinker',
              'last':'Should have brought Natty Light'
    }
    
    people = Person.objects.all()
    averages = {}

    # This is ghetto ;-)
    titles = []
    for i in range(len(people)):
        if i == 0:
            titles.append(meta['first'])

        elif i == 1:
            titles.append(meta['second'])

        elif i == 2:
            titles.append(meta['third'])

        elif i == (len(people) - 1):
            titles.append(meta['last'])

        else:
            titles.append(meta['middle'])
            
    for p in people:
        beers = Beer.objects.filter(person__id = p.id)

        try:
            avg = (sum([b.rating for b in beers]) / len(beers))

        except ZeroDivisionError as e:
            avg = 0
            
        averages[p] = avg
   
    sortedAverages = sorted(averages.iteritems(), key=operator.itemgetter(1), reverse=True)

    # This is ghetto ;-)
    finalData = []
    for i, each in enumerate(sortedAverages):
        x = (each[0], (each[1], titles[i]))
        finalData.append(x)
        
    return render_to_response('beerswap/leaderboard.html', {'averages': finalData})
    
