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
            h = HttpResponse(events)
            return h
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
    filEvents = Event.objects.filter(sensor_triggered_id=sensor)
    #filEvents = Event.objects.order_by('-date_created')
    return toHtml(filEvents)


# noinspection PyBroadException
def toHtml(events):
    rows = ""
    link = ""
    for event in events:
        try:
            link = formatLink(event.event_image.url)
        except ValueError:
            link = ""

        rows += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td>" \
                "</tr>".format(event.id, event.event_type.eventType_name, event.date_created,
                               event.time_created, event.user_id.user.username,
                               event.sensor_triggered.sensor_name, link)
    return rows


def formatLink(link):
    l = "<a href=\"{0}\" onclick=\"window.open('{0}', 'Image', 'width=300, height=250'); return false;\"" \
        ">Image</a>".format(link)
    return l