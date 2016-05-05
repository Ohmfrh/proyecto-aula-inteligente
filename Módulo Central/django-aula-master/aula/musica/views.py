import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from usuarios.models import Usersys
from musica.models import Song, UserSong
from .forms import AddSong, SongForm, EditSong
from multimedia.models import Server


# Create your views here.
def index(request):
    users = Usersys.objects.all()
    songs = Song.objects.all()

    add_song_form = AddSong()
    assign_song_form = SongForm()
    edit_song_form = EditSong()

    context = {'users': users, 'songs': songs, 'add_song_form': add_song_form, 'assign_song_form': assign_song_form,
               'edit_song_form': edit_song_form}
    return render(request, 'musica/index.html', context)


def usuario(request):
    users = Usersys.objects.all()
    songs = Song.objects.all()
    add_song_form = AddSong()
    edit_song_form = EditSong()

    if request.method == 'POST':
        assign_song_form = SongForm(request.POST)
        if assign_song_form.is_valid():
            print "????"
            userId = request.POST['UserOwner']
            user = Usersys.objects.get(pk=userId)
            userSongs = UserSong.objects.all()
            userSongs = userSongs.filter(user=userId)

            for song in userSongs:
                print "IN SONG FOR"
                song.delete()
            print request.POST
            list = request.POST.getlist('Canciones')
            print list
            for item in list:
                print "LIST"
                song = Song.objects.get(pk=item)
                usrsng = UserSong(user=user, song=song)
                usrsng.save()


            return HttpResponseRedirect('/musica/')

    else:
        assign_song_form = SongForm()

    print "FOUR"
    context = {'users': users, 'songs': songs, 'add_song_form': add_song_form, 'assign_song_form': assign_song_form,
               'edit_song_form': edit_song_form}
    return render(request, 'musica/index.html', context)


def agregar(request):
    users = Usersys.objects.all()
    songs = Song.objects.all()
    assign_song_form = SongForm()
    edit_song_form = EditSong()

    if request.method == 'POST':
        add_song_form = AddSong(request.POST)
        print "information sent"

        if add_song_form.is_valid():
            print "Query stuff"
            path = request.POST['Path']
            name = request.POST['Name']
            serverId = request.POST['ServerList']
            artist = request.POST['Artist']
            album = request.POST['Album']
            image = request.POST['Image']

            server = Server.objects.get(pk=serverId)
            newSong = Song(name=name, path=path, server=server, artist=artist, album=album, image=image)

            newSong.save()
            
            return HttpResponseRedirect('/musica/')
    else:
        add_song_form = AddSong()

    context = {'users': users, 'songs': songs, 'add_song_form': add_song_form, 'assign_song_form': assign_song_form,
               'edit_song_form': edit_song_form}
    return render(request, 'musica/index.html', context)


def lista(request):
    list = []
    userId = request.GET['userId']
    songs = Song.objects.all()
    songs = songs.filter(users=userId)

    for row in songs:
        list.append({'songId': row.pk})

    # data = serializers.serialize("json", list)
    data = json.dumps(list)

    # data['user'] = Usersys.objects.get(pk=userId)
    return HttpResponse(data, content_type='application/json')


def cancion(request):
    data = {}
    list = []
    songId = request.GET['songId']
    song = Song.objects.get(pk=songId)

    data['name'] = song.name
    data['path'] = song.path
    data['id'] = song.pk
    data['artist'] = song.artist
    data['album'] = song.album
    data['image'] = song.image
    data['server'] = song.server.pk

    print data['server']

    list.append(data)
    data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')


def editar(request):
    users = Usersys.objects.all()
    songs = Song.objects.all()
    assign_song_form = SongForm()
    add_song_form = AddSong()

    if request.method == 'POST':
        edit_song_form = EditSong(request.POST)

        if edit_song_form.is_valid():
            print "Query stuff"
            path = request.POST['editPath']
            name = request.POST['editName']
            serverId = request.POST['editServerList']
            songId = request.POST['editId']
            album = request.POST['editAlbum']
            image = request.POST['editImage']
            artist = request.POST['editArtist']

            server = Server.objects.get(pk=serverId)

            song = Song.objects.get(pk=songId)

            song.path = path
            song.name = name
            song.server = server
            song.album = album
            song.image = image
            song.artist = artist

            song.save()

            print song


            return HttpResponseRedirect('/musica/')
    else:
        edit_song_form = EditSong()

    context = {'users': users, 'songs': songs, 'add_song_form': add_song_form, 'assign_song_form': assign_song_form,
               'edit_song_form': edit_song_form}
    return render(request, 'musica/index.html', context)