import datetime


def timing(get_response):
    def middleware(request):
        print("hello")
        request.current_time=datetime.datetime.now()
        response=get_response(request)
        return response
    return middleware


