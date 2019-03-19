$(function(){

        $.ajax({
        url: "http://127.0.0.1:8000/admin/delete_data/",
        type: "GET",
        dataType: "json",
    }).done(function(result){


        let data = $('#table tbody');

        for(let i of result) {
            data.append(`<tr><td>${i}</td><td>${i}</td><td></td>/tr>`);
        }
        for(let i of result){
            i.title.on('click', function(){
                $('div')
            })
        }
    }).fail(function(){

    })
});