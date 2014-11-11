from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from ac3app.models import Event


@login_required
def filter_view(request):
    eventHtml = "Hello"
    if request.method == 'GET':
        try:
            filters = request.GET
        except ObjectDoesNotExist:
            filters = None

        if filters is not None:
            #TODO Get data for table from filter parameters Need method
            events = get_filtered_events(filters)
            return HttpResponse(events)
        else:
            return HttpResponse(eventHtml)
    return HttpResponse("This is a test")


def get_filtered_events(filter):
    user = filter['username']
    event = filter['event']
    sensor = filter['sensor']
    date1 = filter['date1']
    date2 = filter['date2']

    #filEvents = Event.objects.filter(event_type=event).values()
    filEvents = Event.objects.filter(user_id_id__user_id__id=user).values()
    return filEvents