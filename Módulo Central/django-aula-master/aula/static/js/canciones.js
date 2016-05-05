/**
 * Created by daniel on 1/05/16.
 */
function showSongList(){
    $('.toggle-class').fadeOut(250, function (){
        console.log(this);
        console.log('DONE');

    });

    setTimeout(function () {
        $('#full-song-list').fadeIn('fast');
    },250);
}

function showUserSongs(userId){
    $('.toggle-class').fadeOut(250);
    setTimeout(function () {
        data = {userId: userId};
        $.get( "/musica/lista/",data, function (data){
            $('input:checkbox').removeAttr('checked');

            if (data.length != 0) {
                for (var i=0; i<data.length; i++) {
                    console.log(data[i]);
                    $('#id_Canciones_'+data[i]['songId']).prop('checked', true);
                }
            }
            $('#id_UserOwner').val(userId)
        });

        $('#user-song-list').fadeIn('fast');
    },250);
}

function addNewSong() {
    $('#add-new-song').slideDown(250);
}

function editSong(songId) {

    $('#id_editName').val('');
    $('#id_editServerList').val('0');
    $('#id_editPath').val('');
    $('#id_editArtist').val('');
    $('#id_editAlbum').val('');
    $('#id_editImage').val('');
    $('#id_editId').val('');

    data = {songId: songId}

    $.get( "/musica/cancion/",data, function (data){
        console.log('SUCCESS');
        console.log(data);
        $('#id_editName').val(data['name']);
        $('#id_editServerList').val(data['server']);
        $('#id_editPath').val(data['path']);
        $('#id_editId').val(data['id']);
        $('#id_editAlbum').val(data['album']);
        $('#id_editImage').val(data['image']);
        $('#id_editArtist').val(data['artist']);

        $('#edit-song').fadeIn(250);
    });
}