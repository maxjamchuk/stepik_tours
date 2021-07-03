from django.http import Http404, HttpRequest
from django.shortcuts import render


from .data import departures, tours


def main_view(request: HttpRequest):
    return render(request, 'tours/index.html')


def departure_view(request: HttpRequest, departure_id: str):
    try:
        departure = departures[departure_id]
    except KeyError:
        raise Http404

    return render(request, 'tours/departure.html', {
        'departure': departure
    })


def tour_view(request: HttpRequest, tour_id: int):
    try:
        tour = tours[tour_id]['title']
        country = tours[tour_id]['country']
    except KeyError:
        raise Http404

    return render(request, 'tours/tour.html', {
        'tour': tour,
        'country': country
    })
