$(document).ready(() => {
    const form = $('#mce_form');
    const url = '/mce_signup/';

    form.submit((e) => {
        e.preventDefault();

        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: (data) => {
                console.log(data);
            }
        })
            .done(function() {
                console.log('Done');
            })
            .fail(function() {
                console.log('Error');
            })
            .always(function() {
                console.log('Complete');
            });
    });
});