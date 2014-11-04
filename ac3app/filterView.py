from django.http import HttpResponse


def filter_view(request):
    context = request
    return HttpResponse("This is a test")