# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
import json
import hashlib

from django.shortcuts import redirect, render_to_response, RequestContext
from django.template.defaulttags import csrf_token
from django.http import HttpResponse

from iglesia.models import Ubigeo, TipoUsuario, Usuario, TipoDocumento


# Create your views here.


def login(request):
    if request.method == 'POST':

        return redirect("/home")

    else:
        return render_to_response('login.html', {}, context_instance=RequestContext(request))


def home(request):
    # tabernaculodeDios.globals['csrf_token'] = generate_csrf_token()

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def registrousuario(request):
    titulo = "Registro de usuario | Tabernáculo de Dios"
    nombreModulo = "Usuarios"
    nombreMenu = "Registro de usuario"
    tituloParte1 = "Registro "
    tituloParte2 = "de usuario"

    if request.method == 'POST':

        if request.POST["metodo"] == "actualizar":

            usuario = Usuario.objects.get(id=request.POST["id"])
            usuario.nombres = request.POST['nombre'].upper()
            usuario.apellidos = request.POST['apellidos'].upper()
            usuario.tipodocumento_id = request.POST['tipodocumento']
            usuario.numerodocumento = request.POST['numerodocumento']
            usuario.direccion = request.POST['direccion'].upper()
            usuario.codigoubigeo_id = request.POST['ubigeo']
            usuario.telefono = request.POST['telefono']
            usuario.celular = request.POST['celular']
            usuario.correoelectronico = request.POST['correoelectronico']
            usuario.fechanacimiento = request.POST['fechanacimiento']
            usuario.tipousuario_id = request.POST['tipousuario']
            usuario.sexo = request.POST['sexo']
            usuario.estadocivil = request.POST['estadocivil']

            if request.POST.get("admin") != 'on':
                usuario.admin = False
            else:
                usuario.admin = True

            if request.POST['password'] != "":
                usuario.password = hashlib.sha512(request.POST['password']).hexdigest()

            usuario.save()
            return redirect('/usuario/detalleusuario.html?id=' + str(usuario.id) + '&mensaje=2')
        else:

            usuario = Usuario()
            usuario.nombres = request.POST['nombre'].upper()
            usuario.apellidos = request.POST['apellidos'].upper()
            usuario.tipodocumento_id = request.POST['tipodocumento']
            usuario.numerodocumento = request.POST['numerodocumento']
            usuario.direccion = request.POST['direccion'].upper()
            usuario.codigoubigeo_id = request.POST['ubigeo']
            usuario.telefono = request.POST['telefono']
            usuario.celular = request.POST['celular']
            usuario.correoelectronico = request.POST['correoelectronico']
            usuario.fechanacimiento = request.POST['fechanacimiento']
            usuario.tipousuario_id = request.POST['tipousuario']
            usuario.sexo = request.POST['sexo']
            usuario.estadocivil = request.POST['estadocivil']

            if request.POST["admin"] == 'on':
                usuario.admin = True
            else:
                usuario.admin = False

            if request.POST['password'] != '':
                usuario.password = hashlib.sha512(request.POST['password']).hexdigest()

            usuario.save()
            return redirect('/usuario/detalleusuario.html?id=' + str(usuario.id) + '&mensaje=1')
    else:
        listaTipoUsuario = TipoUsuario.objects.all()
        listaTipoDocumento = TipoDocumento.objects.all()
        return render_to_response('usuario/registrousuario.html', locals(), context_instance=RequestContext(request))


def detalleusuario(request):
    titulo = "Detalle de usuario | Tabernáculo de Dios"
    nombreModulo = "Usuarios"
    nombreMenu = "Detalle de usuario"
    tituloParte1 = "Detalle "
    tituloParte2 = "de usuario"

    tipoDeMensajeId = int(request.GET['mensaje'])

    if tipoDeMensajeId == 1:
        mensaje = crearMensajeSatisfactorio("El registro se realiz&oacute; de forma satisfactoria")
    else:
        mensaje = crearMensajeSatisfactorio("La actualizaci&oacute;n se realiz&oacute; de forma satisfactoria")

    datosUsuario = Usuario.objects.get(id=int(request.GET['id']))
    ubigeousuario = Ubigeo.objects.get(codigo=datosUsuario.codigoubigeo_id)
    tipoDocumentoUsuario = TipoDocumento.objects.get(id=datosUsuario.tipodocumento_id)
    tipoUsuario = TipoUsuario.objects.get(id=datosUsuario.tipousuario_id)
    listaTipoUsuario = TipoUsuario.objects.all()
    listaTipoDocumento = TipoDocumento.objects.all()

    return render_to_response('usuario/detalleusuario.html', locals(), context_instance=RequestContext(request))


def buscarubigeopornombre(request):
    listaUbigeo = Ubigeo.objects.filter(ubigeo__icontains=request.GET['term'])[:50]
    listaCompleta = []
    indediceDeFile = 0

    for ubigeo in listaUbigeo:
        indediceDeFile = indediceDeFile + 1
        listaCompleta.insert(indediceDeFile, {'codigo': ubigeo.codigo, 'ubigeo': ubigeo.ubigeo})

    return HttpResponse(json.dumps(listaCompleta), content_type="application/json")


def crearMensajeSatisfactorio(mensaje):
    crearDiv = '<div class="alert alert-success">' \
               '<button data-dismiss="alert" class="close">' \
               '&times;</button>' \
               '<i class="fa fa-check-circle"></i>' \
               '<strong>Muy Bien!</strong> ' + mensaje + \
               '</div>'

    return crearDiv


def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf_token._get_new_csrf_key()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token
