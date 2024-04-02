$(document).ready(function () {
    $("#search").keyup(function () {
        var input = $("#search").val();
        if (input.length > 3) {
            url = 'http://127.0.0.1:5000/api/services/';
            url = url.concat(input);
            $.get(url, function (data) {
                for (let i = 0; i < data.length; i++) {
                    $("#options").html(`<li class="option">${data[i]}</li>`);
                }
            });
        }
    });
    $(document).on('click', 'li', function () {
        var serv = $(this).text();
        $("#search").val(serv);
        $("#options").html(" ");
    });
});