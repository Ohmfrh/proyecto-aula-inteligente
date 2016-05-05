import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Server
from .forms import ServerForm, EditServerForm


# Create your views here.
def index(request):
    servers = Server.objects.all()
    form = ServerForm()
    formEdit = EditServerForm()

    context = {'servers': servers, 'form': form, 'formEdit': formEdit}
    return render(request, 'multimedia/index.html', context)


def crear(request):
    formEdit = EditServerForm
    servers = Server.objects.all()
    if request.method == 'POST':
        form = ServerForm(request.POST)

        if form.is_valid():
            print "SUCCESS"
            usr = request.POST['usuario']
            passwd = request.POST['contrasena']
            addr = request.POST['direccion']

            print usr + ' ' + passwd + ' ' + addr
            newServer = Server(address=addr, user=usr, password=passwd)
            newServer.save()

            return HttpResponseRedirect('/multimedia/')
    else:
        form = ServerForm()

    context = {'servers': servers, 'form': form, 'formEdit': formEdit}
    return render(request, 'multimedia/index.html', context)


def editar(request):
    servers = Server.objects.all()
    form = ServerForm()
    if request.method == 'POST':
        formEdit = EditServerForm(request.POST)

        if formEdit.is_valid():
            print request.POST
            serverId = request.POST['serverId']
            address = request.POST['dirEdit']
            password = request.POST['passEdit']
            user = request.POST['usrEdit']

            server = Server.objects.get(pk=serverId)
            server.address = address
            server.password = password
            server.user = user

            server.save()

            return HttpResponseRedirect('/multimedia/')
    else:
        formEdit = EditServerForm()

    context = {'servers': servers, 'form': form, 'formEdit': formEdit}
    return render(request, 'multimedia/index.html', context)


def servidor(request):
    server = Server.objects.get(pk=request.GET['serverId'])
    data = {'address': server.address, 'user': server.user, 'password': server.password}

    data = json.dumps(data)

    return HttpResponse(data)


def eliminar(request):
    print "EN ELIMINAR"
    serverId = request.POST['serverId']

    server = Server.objects.get(pk=serverId)
    server.delete()

    data = {'message': 'done'}
    return HttpResponse(data)
