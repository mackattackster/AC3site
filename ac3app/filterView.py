from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from ac3app.models import Event


@login_required
def filter_view(request):
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
            return HttpResponse()
    return HttpResponse("This is a test")


def get_filtered_events(filter):
    user = filter['username']
    event = filter['event']
    sensor = filter['sensor']
    date1 = filter['date1']
    date2 = filter['date2']
    fil = toSQL(filter)
    #filEvents = Event.objects.filter(event_type=event).values()
    filEvents = Event.objects.filter(sensor_triggered_id=sensor)
    #filEvents = Event.objects.order_by('-date_created')
    #return toHtml(filEvents)'
    return fil


# noinspection PyBroadException
def toHtml(events):
    rows = ""
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


def toSQL(filters):
    #Event.objects.raw("SQL")
    #id date_created event_type_id sensor_triggered_id user_id_id
    sql = "SELECT * FROM ac3app_event WHERE"
    for fil in filters:
        if filters[fil] != '0':
            if fil == 'username':
                sql += " user_id_id = {0} AND".format(filters[fil])
            elif fil == 'sensor':
                sql += " sensor_triggered_id = {0} AND".format(filters[fil])
            elif fil == 'event':
                sql += " event_type_id = {0} AND".format(filters[fil])
        else:
            t = 1
    sql = sql[:-4]
    temp = toHtml(Event.objects.raw(sql))
    return temp


def goThroughEvents(event):
    s = {}
    for e in event:
        s += "{0}, {1}, {2}".format(e.id, e.event_type, e.sensor_triggered)
    return s