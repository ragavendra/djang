from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, this is the polls index Raga")
