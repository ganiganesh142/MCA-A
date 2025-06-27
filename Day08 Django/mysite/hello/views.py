from django.http import HttpResponse
def home(request):
    return HttpResponse("hello,Django!")

# Create your views here.
