from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Bem Vindo ao Projeto </h1>")
