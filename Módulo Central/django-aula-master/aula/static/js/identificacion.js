/**
 * Created by daniel on 30/04/16.
 */
$('img').click(function () {
    $('#edit-id-content').html('');

    var data = {userId: this.id};
    $('#myModal').modal('show');
    $.get("/identificacion/identificar/", data, function (data) {
        console.log('???');
        console.log(data);

        for (var i = 0; i < data.length; i++){

            var row = document.createElement('div');
            var colInput = document.createElement('div');
            var colButton = document.createElement('div');
            var input = document.createElement('input');
            var delButton = document.createElement('button');

            row.className = '';
            colInput.className = 'col-md-6';
            colButton.className = 'col-md-5';
            input.className = 'form-control id-edit-data input-form';
            input.type = 'text';
            delButton.className = 'btn btn-danger pull-right deleteId';
            delButton.innerHTML = 'Borrar';
            delButton.name = data[i]['id'];

            colInput.appendChild(input);
            colButton.appendChild(delButton);
            row.appendChild(colInput);
            row.appendChild(colButton);
            input.name = data[i]['id'];
            input.value = data[i]['string'];

            $('#edit-id-content').append(row);

        }
        $('.deleteId').click(function(){
            data = {id: this.name};
            $.post("/identificacion/borrar/", data, function (data) {
                console.log('success');
                location.reload();
            });


        });
    });
});

function send() {
    console.log('Send');
    var cards = [];
    $('.id-edit-data').each(function (index)  {
        console.log(this.value);
        console.log(this.name);
        cards.push({string: this.value, id: this.name});
    });


    data =  {cards: JSON.stringify(cards)};
    $.post("/identificacion/editar/", data, function (data) {
        console.log('success');
        location.reload();
    });

}
