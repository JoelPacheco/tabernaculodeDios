# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
from django.shortcuts import render,redirect, render_to_response, RequestContext
from django.http.response import HttpResponseRedirect
from django.template.defaulttags import csrf_token
import random
import os
# Create your views here.
def login(request):
    if request.method == 'POST':

        request_token = request.POST.get('csrfmiddlewaretoken')

        if request_token != csrf_token:
            numeroAleatorio = str(random.randint(1111111111111, 9999999999999))
            return redirect("home/"+numeroAleatorio)
        else:
            return redirect("/")
    else:
        return render_to_response('login.html',{},context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html',{},context_instance=RequestContext(request))

def registrousuario(request):
    titulo = "Registro de usuario | Tabernáculo de Dios"
    nombreModulo = "Usuarios"
    nombreMenu = "Registro de usuario"
    tituloParte1 = "Registro "
    tituloParte2 = "de usuario"
    return render_to_response('registrousuario.html',locals(),context_instance=RequestContext(request))