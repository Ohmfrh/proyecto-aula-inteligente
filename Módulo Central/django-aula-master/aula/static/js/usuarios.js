/**
 * Created by daniel on 4/05/16.
 */
function editUser(usrId) {
    $('#edit-user').slideDown(500);
    $('#id_editName').val('');
    $('#id_editLast_names').val('');
    $('#id_editEmail').val('');
    $('#id_editId').val('');
    console.log(usrId);

    data = {usrId: usrId}

    $.get( "/usuarios/usuario/",data, function (data){
        console.log('SUCCESS');
        console.log(data);

        $('#id_editName').val(data['name']);
        $('#id_editLast_names').val(data['last_names']);
        $('#id_editEmail').val(data['email']);
        $('#id_editId').val(data['id']);

    });
}