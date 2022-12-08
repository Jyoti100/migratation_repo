from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.{}".format(request.current_time))