$( document ).ready(function() {
    $('#registration_form').validate({
        rules: {
            password_check: {
                equalTo: "#password_input"
              }
        }
    })
    $('#login_form').validate()
})
