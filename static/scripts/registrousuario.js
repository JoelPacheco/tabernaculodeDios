/**
 * Created by joelpacheco on 27/03/15.
 */
var registroUsuario = function () {

    // Carga la lista de ubigeo en los select o combos
    var cargarUbigeo = function () {
        $("#ubigeo").select2();
    };


    var mostrarFecha = function () {

        $('#fechanacimiento').datepicker({
            language: 'es',
            endDate: '+0y',
            startView:'year',
            autoclose: true
        });
    };

    return {
        init: function () {
            cargarUbigeo();
            mostrarFecha();
        }
    }

}();