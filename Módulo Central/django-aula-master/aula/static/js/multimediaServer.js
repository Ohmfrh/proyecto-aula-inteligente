/**
 * Created by daniel on 1/05/16.
 */
function addServer() {
    $('.hide-class').fadeOut(250);

    setTimeout(function () {
        $('#id_direccion').val('');
        $('#id_usuario').val('');
        $('#id_contrasena').val('');
        $('#new-server-form').fadeIn(250);
    }, 250);
    console.log('Add Server');
}

function editServer(serverId) {
    $('.hide-class').fadeOut(250, function () {
        $('#id_dirEdit').val('');
        $('#id_usrEdit').val('');
        $('#id_passEdit').val('');
        $('#id_serverId').val(serverId);
    });

    data = {serverId: serverId};

    $.get( "/multimedia/servidor/",data, function (data){
        data = JSON.parse(data);
        setTimeout(function () {
            $('#id_dirEdit').val(data['address']);
            $('#id_usrEdit').val(data['user']);
            $('#id_passEdit').val(data['password']);
            $('#delete-server').attr('name', serverId);
            $('#edit-server-form').fadeIn(250);
        }, 250);

    });
}

function deleteServer(serverId) {
    console.log('Delete: ' + serverId);

    data = {serverId: serverId};
    $.post( "/multimedia/eliminar/",data, function (data){
        console.log(data);
        console.log('Done');
        location.reload()
    });
}