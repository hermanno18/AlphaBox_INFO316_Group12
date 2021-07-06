from django.shortcuts import render, get_object_or_404
from ..models import Utilisateur
from .inscr_conn_decon import UserExit
from alphabox.others_models.setting import *
""" la vue ci est là pour gerer les vues concernant le dashboard afin de mieux découper le code """

def dashboard_evolution(request, userName = 'default'):
    context = {}
    dashboard=None
    if( 'login' in request.session):
        joueurs=Joueur.objects.all()

        for joueur in joueurs:
            if joueur.UserName == request.session['login']:
                dashboard=joueur.j_Dashboard
                break
        context ={
            "jouer" : joueur.UserName,
            "MotTrouve" : joueur.nbMotTrouve,
            "NoteDictee" : joueur.bestNoteDictee,
            "DefiGagne" : joueur.nbDefiGagne,
            "nbPartieJouer" : joueur.nbPartieJouer,
            "nbPartiefGagne" : joueur.nbPartiefGagne,
            "Points" : joueur.nbPoints,
            "langues" : joueur.languesApprise 
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
