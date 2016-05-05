from django.core import serializers
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from usuarios.models import Usersys

from .models import Type, Identify
from .forms import AddId


# Create your views here.
def index(request):
    users = Usersys.objects.all()

    form = AddId()

    context = {'users': users, 'form': form}
    return render(request, 'identificacion/index.html', context)


def nuevo(request):
    users = Usersys.objects.all()

    # print request
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddId(request.POST)

        # check whether it's valid:
        if form.is_valid():
            rfid = Type.objects.get(name='rfid')
            user = Usersys.objects.get(pk=request.POST['Usuario'])
            new = Identify(string=request.POST['String'], usersys=user, type=rfid)
            new.save()

            print rfid
            print user


            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/identificacion/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddId()

    context = {'users': users, 'form': form}
    return render(request, 'identificacion/index.html', context)


def editar(request):
    print "En editar"

    cards = json.loads(request.POST.get('cards'))

    for card in cards:
        id = card['id']
        string = card['string']
        idcard = Identify.objects.get(pk=id)
        idcard.string = string
        idcard.save()

    data = 'success'
    return HttpResponse(data)


def identificar(request):
    print "En identify"
    list = []
    userId = request.GET['userId']
    idSet = Identify.objects.all()
    idSet = idSet.filter(usersys=userId)

    for row in idSet:
        list.append ({'user': row.usersys.name, 'string': row.string, 'id': row.pk})

    # data = serializers.serialize("json", list)
    data = json.dumps(list)

    # data['user'] = Usersys.objects.get(pk=userId)
    return HttpResponse(data, content_type='application/json')


def borrar(request):
    id = request.POST['id']
    card = Identify.objects.get(pk=id)

    card.delete()

    data = 'success'
    return HttpResponse(data)