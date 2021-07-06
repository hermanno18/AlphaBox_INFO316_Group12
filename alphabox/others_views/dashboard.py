from django.shortcuts import render, get_object_or_404
from ..models import Utilisateur
from .inscr_conn_decon import UserExit
""" la vue ci est là pour gerer les vues concernant le dashboard afin de mieux découper le code """

def dashboard_evolution(request, userName = 'default'):
    context = {}
    if(userName != "default"):
        context = {
            "User" : get_object_or_404(Utilisateur, UserName=userName)
        }
    return render(request, 'alphabox/backOffice/dashboard/evolution.html', context)

def dashboard_profile(request , userName = 'default'):
    context = {}
    if(userName != "default"):
        context = {
            "User" : get_object_or_404(Utilisateur, UserName=userName)
        }
    return render(request, 'alphabox/backOffice/dashboard/profile.html', context)

def dashboard_program(request, userName = 'default'):
    context = {}
    if(userName != "default"):
        context = {
            "User" : get_object_or_404(Utilisateur, UserName=userName)
        }
    return render(request, 'alphabox/backOffice/dashboard/program.html', context)

def dashboard_friends(request, userName = 'default'):
    context = {}
    if(userName != "default"):
        context = {
            "User" : get_object_or_404(Utilisateur, UserName=userName)
        }
    return render(request, 'alphabox/backOffice/dashboard/friends.html', context)

def dashboard_others(request, userName):
    context = {}
    if(userName != "default"):
        context = {
            "User" : get_object_or_404(Utilisateur, UserName=userName)
        }
    return render(request, 'alphabox/backOffice/dashboard/others.html', context)
