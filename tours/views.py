from functools import reduce
from random import shuffle

from django.http import Http404, HttpRequest
from django.shortcuts import render


from tours.data import departures, tours, title, subtitle, description


for k in tours.keys():
    tours[k]['id'] = k


def main_view(request: HttpRequest):

    random_tours = list(tours.values())
    shuffle(random_tours)
    random_tours = random_tours[:6]

    return render(request, 'tours/index.html', context={'title': title,
                                                        'subtitle': subtitle,
                                                        'description': description,
                                                        'tours': random_tours})


def departure_view(request: HttpRequest, departure_id: str):
    try:
        departure = departures[departure_id]
        departure_tours = [tour for tour in list(tours.values()) if tour['departure'] == departure_id]
        common_info = {'max_price': reduce(lambda a, b: a if (a > b) else b, [i['price'] for i in departure_tours]),
                       'min_price': reduce(lambda a, b: a if (a < b) else b, [i['price'] for i in departure_tours]),
                       'max_nights': reduce(lambda a, b: a if (a > b) else b, [i['nights'] for i in departure_tours]),
                       'min_nights': reduce(lambda a, b: a if (a < b) else b, [i['nights'] for i in departure_tours])}
    except KeyError:
        raise Http404

    return render(request, 'tours/departure.html', {
        'current_departure': departure,
        'tours': departure_tours,
        'common_info': common_info
    })


def tour_view(request: HttpRequest, tour_id: int):
    try:
        tour = tours[tour_id]
    except KeyError:
        raise Http404

    tour['departure'] = departures[tour['departure']]

    return render(request, 'tours/tour.html', context=tour)
