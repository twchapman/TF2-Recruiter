from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    if request.user.is_authenticated():
        return HttpResponse(request.user)
    else:
        return HttpResponseRedirect('/openid/')