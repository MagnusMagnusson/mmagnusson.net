function login() {
    console.log("logging in");
    D = {
        'user':$("#uName").val(),
        'password':$("#pWord").val()
    }
    console.log(D);
    $.ajax({
        type: "POST",
        url: login_api,
        dataType: 'json',
        data: D,
        success: function (d) {
            if (d.success) {
                location.reload();
            }
            else {
                alert(d.error);
            }

        }
    });
}

$(document).ready(function () {
    console.log("Redz");
    $("#login").on('click', function (e) {
        login();
    })
});