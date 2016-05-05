import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from usuarios.models import Usersys
from .models import Pipeline

# Create your views here.
def index(request):
    users = Usersys.objects.all()
    context = {'users': users}
    return render(request, 'home/index.html', context)


@csrf_exempt
def pipeline(request):

    try:
        pipe = Pipeline.objects.all()[:1].get()
        data = pipe.pipe
        pipe.delete()
    except:
        data = {}
        data['accion'] = "Nada"
        data = json.dumps(data)


    return HttpResponse(data, content_type='application/json')
