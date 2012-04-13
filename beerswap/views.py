# Create your views here.
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
    people = Person.objects.all()
    beers = Beer.objects.all()

    data = {}
    for p in people:
        data[p] = []

    for b in beers:
        data[b.person].append(b.rating)

    for k,v in data.items():
        if not len(v):
            continue
            
        currentSum = 0
        for each in v:
            currentSum += each

        avg = currentSum / len(v)

        data[k] = avg

    for k, v in data.items():
        if not isinstance(v, int):
            data[k] = 0
    
    sortedAverages = sorted(data.iteritems(), key=operator.itemgetter(1), reverse=True)

    return render_to_response('beerswap/leaderboard.html', {'averages': sortedAverages})
    
