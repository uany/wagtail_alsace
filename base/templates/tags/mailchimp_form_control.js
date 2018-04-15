$(document).ready(() => {
    const form = $('#mce_form');
    const url = '/mce_signup/';

    form.submit((e) => {
        e.preventDefault();

        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            beforeSend:() => {
                $('#mce_form_errors').hide();

            },
            success: (data) => {
                form.slideUp();
                $('.mce_thanks').show();
            }
        })
            .done(function(data) {
                console.log(data);
            })
            .fail(function(error) {
                let error_message = error.responseJSON.detail;
                $('#mce_form_errors')
                    .text(error_message);

                $('#mce_form_errors')
                    .slideDown();
            })
            .always(function() {
                console.log('Complete');
            });
    });
});