from tours.data import departures as dep


def departures(request):
    return {'departures': dep}
