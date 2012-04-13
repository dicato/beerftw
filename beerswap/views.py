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
    averages = {}
    
    for p in people:
        beers = Beer.objects.filter(person__id = p.id)

        try:
            avg = (sum([b.rating for b in beers]) / len(beers))

        except ZeroDivisionError as e:
            avg = 0
            
        averages[p] = avg
   
    sortedAverages = sorted(averages.iteritems(), key=operator.itemgetter(1), reverse=True)
    return render_to_response('beerswap/leaderboard.html', {'averages': sortedAverages})
    
