/**
 * Created by joelpacheco on 23/03/15.
 */

var Login = function () {

    var runLoginButtons = function () {
        $('.forgot').bind('click', function () {
            $('.box-login').hide();
            $('.box-forgot').show();
        });
        $('.register').bind('click', function () {
            $('.box-login').hide();
            $('.box-register').show();
        });
        $('.go-back').click(function () {
            $('.box-login').show();
            $('.box-forgot').hide();
            $('.box-register').hide();
        });
    };

    var validacionLogin = function () {


        var formLogin = $('#formlogin');
        var errorHandler1 = $('.errorHandler', formLogin);
        var successHandler1 = $('.successHandler', formLogin);

        $.validator.addMethod("validateemail", function (value, element) {
            return this.optional(element) || /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(value);
        }, "Ingrese un correo v&aacute;lido");


        formLogin.validate({

            errorElement: "span", // contain the error msg in a span tag
            errorClass: 'help-block',
            errorPlacement: function (error, element) { // render error placement for each input type
                if (element.attr("type") == "radio" || element.attr("type") == "checkbox") { // for chosen elements, need to insert the error after the chosen container
                    error.insertAfter($(element).closest('.form-group').children('div').children().last());
                } else if (element.attr("name") == "dd" || element.attr("name") == "mm" || element.attr("name") == "yyyy") {
                    error.insertAfter($(element).closest('.form-group').children('div'));
                } else {
                    error.insertAfter(element);
                    // for other inputs, just perform default behavior
                }
            },
            ignore: "",
            rules: {
                correoelectronico: {
                    required: true,
                    validateemail: true
                },
                password: {
                    required: true
                }
            },
            messages: {
                correoelectronico: { required: "Por ingrese su correo electr&oacute;nico", validateemail: "Correo inv&aacute;lido"},
                password: {required: "Ingrese su contrase&ntilde;a"}
            },

            invalidHandler: function (event, validator) { //display error alert on form submit
                successHandler1.hide();
                errorHandler1.show();
            },
            highlight: function (element) {
                $(element).closest('.help-block').removeClass('valid');
                // display OK icon
                $(element).closest('.form-group').removeClass('has-success').addClass('has-error').find('.symbol').removeClass('ok').addClass('required');
                // add the Bootstrap error class to the control group
            },
            unhighlight: function (element) { // revert the change done by hightlight
                $(element).closest('.form-group').removeClass('has-error');
                // set error class to the control group
            },
            success: function (label, element) {
                label.addClass('help-block valid');
                // mark the current input as valid and display OK icon
                $(element).closest('.form-group').removeClass('has-error').addClass('has-success').find('.symbol').removeClass('required').addClass('ok');
            },
            submitHandler: function (form) {
                successHandler1.show();
                errorHandler1.hide();

                var passwordActual = $("#password").val();
                var password = $.md5(passwordActual, 'MiPasswordPersonal123456');

                $("#password").val(password);


                form.submit();
                // submit form

                //$('#form').submit();
            }
        });


    };
    return {
        init: function () {
            validacionLogin();
            runLoginButtons();
        }
    }

}();