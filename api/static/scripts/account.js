$(document).ready(function () {
    $("#profile").click(function () {
        $("#profile").addClass("active");
        $("#services").removeClass("active");
        $("#myservices").addClass("hide");
        $("#form").removeClass("hide");
    });
    $("#services").click(function () {
        $("#profile").removeClass("active");
        $("#services").addClass('active');
        $("#myservices").removeClass("hide");
        $("#form").addClass("hide");
    });
});