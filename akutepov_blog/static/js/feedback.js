/**
 * Feedback
 */

$(document).ready(function ($) {

    $('#formFeedback').submit(function (e) {
        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: $(this).serialize(),
            success: function (data) {
                $('#modalFeedback').modal('hide');
                if (data.result == "ok") {
                    $('#modalAlert').modal();
                }
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log("Error: " + errorThrown + xhr.status + xhr.responseText);
            }
        });

        e.preventDefault();
    });

});