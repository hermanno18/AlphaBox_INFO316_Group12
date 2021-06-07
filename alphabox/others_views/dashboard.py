from django.shortcuts import render
""" la vue ci est là pour gerer les vues concernant le dashboard afin de mieux découper le code """

def dashboard_evolution(request):
    return render(request, 'alphabox/backOffice/dashboard/evolution.html')

def dashboard_profile(request):
    return render(request, 'alphabox/backOffice/dashboard/profile.html')

def dashboard_program(request):
    return render(request, 'alphabox/backOffice/dashboard/program.html')

def dashboard_friends(request):
    return render(request, 'alphabox/backOffice/dashboard/friends.html')

def dashboard_others(request):
    return render(request, 'alphabox/backOffice/dashboard/others.html')
