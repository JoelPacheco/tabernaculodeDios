# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
import random
import json

from django.shortcuts import redirect, render_to_response, RequestContext
from django.template.defaulttags import csrf_token
from django.http import HttpResponse

from iglesia.models import Ubigeo, TipoUsuario, Usuario, TipoDocumento

# Create your views here.
def login(request):
    if request.method == 'POST':

        request_token = request.POST.get('csrfmiddlewaretoken')

        if request_token != csrf_token:
            numeroAleatorio = str(random.randint(1111111111111, 9999999999999))
            return redirect("home/" + numeroAleatorio)
        else:
            return redirect("/")
    else:
        return render_to_response('login.html', {}, context_instance=RequestContext(request))


def home(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))


def registrousuario(request):
    titulo = "Registro de usuario | Tabernáculo de Dios"
    nombreModulo = "Usuarios"
    nombreMenu = "Registro de usuario"
    tituloParte1 = "Registro "
    tituloParte2 = "de usuario"

    if request.method == 'POST':
        usuario = Usuario();
        usuario.nombres = request.POST['nombre'].upper();
        usuario.apellidos = request.POST['apellidos'].upper();
        usuario.tipodocumento_id = request.POST['tipodocumento'];
        usuario.numerodocumento = request.POST['numerodocumento'];
        usuario.direccion = request.POST['direccion'].upper();
        usuario.codigoubigeo_id = request.POST['ubigeo'];
        usuario.telefono = request.POST['telefono'];
        usuario.celular = request.POST['celular'];
        usuario.correoelectronico = request.POST['correoelectronico'];
        usuario.fechanacimiento = request.POST['fechanacimiento']
        usuario.tipousuario_id = request.POST['tipousuario'];
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
    mensaje = crearMensajeSatisfactorio("El registro se realiz&oacute; de forma satisfactoria", tipoDeMensajeId)

    datosUsuario = Usuario.objects.get(id=int(request.GET['id']))
    listaTipoUsuario = TipoUsuario.objects.all()
    listaTipoDocumento = TipoDocumento.objects.all()
    listaUbigeo = Ubigeo.objects.get(codigo=datosUsuario.codigoubigeo)

    return render_to_response('usuario/detalleusuario.html', locals(), context_instance=RequestContext(request))


def buscarubigeopornombre(request):
    listaUbigeo = Ubigeo.objects.filter(ubigeo__icontains=request.GET['term'])[:50]
    listaCompleta = []
    indediceDeFile = 0

    for ubigeo in listaUbigeo:
        indediceDeFile = indediceDeFile + 1
        listaCompleta.insert(indediceDeFile, {'codigo': ubigeo.codigo, 'ubigeo': ubigeo.ubigeo})

    return HttpResponse(json.dumps(listaCompleta), content_type="application/json")


def crearMensajeSatisfactorio(mensaje, tipoMensajeId):
    if 1 == tipoMensajeId:
        crearDiv = '<div class="alert alert-success">' \
                   '<button data-dismiss="alert" class="close">' \
                   '&times;</button>' \
                   '<i class="fa fa-check-circle"></i>' \
                   '<strong>Muy Bien!</strong> ' + mensaje + \
                   '</div>'

    return crearDiv