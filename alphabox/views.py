from django.shortcuts import render
from django.http import HttpResponse

#ici j'importe mes autres vues qui sont dans le dossier others_views, je fais ca pour mieux me retrouver dans le code
from .others_views.dashboard import *
from .others_views.games import *
from .others_views.inscr_conn_decon import *
#ici j'importe mes autres vues qui sont dans le dossier others_views, je fais ca pour mieux me retrouver dans le code
def test(request):
    return render(request, "alphabox/test/test.html")
    
def index(request):

    MODULES = {
        "typing": "typing",
        "prononciation": "prononciation",
        "listening": "listening",
        "writing": "writing",
    }
    context = {
        'modules':MODULES   
    }
    return render(request, 'alphabox/home/index.html',context )

