from django.http import HttpResponse


def index(request):
    print("version test hello")
    return HttpResponse("Hello, world. You're at the polls index.{}".format(request.current_time))