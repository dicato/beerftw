from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beerftw.views.home', name='home'),
    # url(r'^beerftw/', include('beerftw.foo.urls')),
    url(r'^$', 'beerswap.views.leaderboard'),
    url(r'^beers/$', 'beerswap.views.beers'),
    url(r'^beers/(?P<beer_id>\d+)/$', 'beerswap.views.beer_detail'),
    url(r'^people/$', 'beerswap.views.people'),
    url(r'^people/(?P<person_id>\d+)/$', 'beerswap.views.person_detail'),
    url(r'^leaderboard/$', 'beerswap.views.leaderboard'),
                       
    # url(r'^beers/(?P<beer_id>\d+)/$', 'beerswap.views.detail'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
