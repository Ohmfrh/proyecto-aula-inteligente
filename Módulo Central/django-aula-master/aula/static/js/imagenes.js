/**
 * Created by daniel on 30/04/16.
 */
function showImageList(){
    $('.toggle-class').fadeOut(250, function (){
        console.log(this);
        console.log('DONE');

    });

    setTimeout(function () {
        $('#full-image-list').fadeIn('fast');
    },250);
}

function showUserImages(userId){
    $('.toggle-class').fadeOut(250);
    setTimeout(function () {
        data = {userId: userId};
        $.get( "/imagenes/lista/",data, function (data){
            $('input:checkbox').removeAttr('checked');

            if (data.length != 0) {
                for (var i=0; i<data.length; i++) {
                    console.log(data[i]);
                    $('#id_Imagenes_'+data[i]['imageId']).prop('checked', true);
                }
            }

            $('#id_UserOwner').val(userId)
        });

        $('#user-image-list').fadeIn('fast');
    },250);


}

function addNewImage() {
    $('#add-new-image').slideDown(250);
}

function editImage(imageId) {
    $('#id_editName').val('');
    $('#id_editServerList').val('0');
    $('#id_editPath').val('');
    $('#id_editId').val('');

    data = {imageId: imageId};

    $.get( "/imagenes/imagen/",data, function (data){
        console.log('SUCCESS');
        console.log(data);
        $('#id_editName').val(data['name']);
        $('#id_editServerList').val(data['server']);
        $('#id_editPath').val(data['path']);
        $('#id_editId').val(data['id']);
        $('#edit-image').fadeIn(250);
    });

    console.log(imageId);
}