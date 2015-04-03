/**
 * Created by joelpacheco on 27/03/15.
 */
var registroUsuario = function () {

    $("#btn").click(function () {

        $("#ubigeo").val("LIMA,LIMA,SAN MARTIN DE PORRES");

    });
    // Carga la lista de ubigeo en los select o combos
    var cargarUbigeo = function () {
        //$("#ubigeo").select2();
        var ubigeonombre = $("#ubigeonombre").val();

        var URL = "/buscarubigeopornombre";

        $("#ubigeo").select2({
            minimumInputLength: 5,
            formatInputTooShort: function () {
                return "Ingrese 5 caracteres";
            },
            ajax: {
                url: URL,
                dataType: 'json',
                type: "GET",
                quietMillis: 50,
                data: function (term) {
                    if ($("#ubigeonombre").val() != "") {
                        term = $("#ubigeonombre").val();
                    }
                    return {
                        term: term.toUpperCase()
                    };
                },
                results: function (data) {

                    return {
                        results: $.map(data, function (item) {
                            return {
                                text: item.ubigeo,
                                id: item.codigo
                            }
                        })
                    };
                }
            }
        });


    };

    var cargarTipoUsuario = function () {
        $("#tipousuario").select2();
    }

    var mostrarFecha = function () {

        $('#fechanacimiento').datepicker({
            language: 'es',
            endDate: '+0y',
            startView: 'year',
            autoclose: true
        });
    };

    var validarNumeroDeDocumento = function () {


        var form1 = $('#formregistrousuario');
        var errorHandler1 = $('.errorHandler', form1);
        var successHandler1 = $('.successHandler', form1);

        $.validator.addMethod("validateemail", function (value, element) {
            return this.optional(element) || /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(value);
        }, "Ingrese un correo v&aacute;lido");

        $.validator.addMethod("lettersonly", function (value, element) {
            return this.optional(element) || /^([a-z ñáéíóú]{2,30})$/i.test(value);
        }, "Solo letras");

        form1.validate({
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
                nombre: {
                    minlength: 3,
                    required: true,
                    lettersonly: true
                },
                apellidos: {
                    minlength: 3,
                    required: true,
                    lettersonly: true
                },
                correoelectronico: {
                    validateemail: true
                },
                tipousuario: {
                    required: true
                },
                numerodocumento: {
                    required: true,
                    digits: true,
                    minlength: 8
                },
                direccion: {
                    required: true,
                    minlength: 8
                },
                ubigeo: {
                    required: true
                },
                fechanacimiento: {
                    required: true
                },
                telefono: {
                    digits: true
                },
                celular: {
                    digits: true
                }
            },
            messages: {
                nombre: {required: "Ingrese nombre", minlength: "Ingrese al menos {0} caracteres"},
                apellidos: {required: "Ingrese apellidos", minlength: "Ingrese al menos {0} caracteres"},
                correoelectronico: {
                    validateemail: "Ingrese un correo v&aacute;lido"
                },
                numerodocumento: {
                    required: "Ingrese n&uacute;mero de documento",
                    digits: "Ingrese solo digitos",
                    minlength: "Ingrese {0} digitos como m&iacute;nimo"
                },
                tipousuario: {
                    required: "Seleccione tipo usuario"
                },
                direccion: {
                    required: "Ingrese direcci&oacute;n",
                    minlength: "Ingrese {0} como m&iacute;nimo"
                },
                ubigeo: {
                    required: "Seleccione ubigeo"
                },
                fechanacimiento: {
                    required: "Ingrese fecha de nacimiento"
                }, telefono: {
                    digits: "Solo n&uacute;meros"
                },
                celular: {
                    digits: "Solo n&uacute;meros"
                },
                gender: "Please check a gender!"
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

                //return true;
                // submit form
                form.submit();
            }
        });
    };

    return {
        init: function () {
            cargarUbigeo();
            cargarTipoUsuario();
            mostrarFecha();
            validarNumeroDeDocumento();
        }
    }

}();