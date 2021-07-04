from django.shortcuts import render
from django.http import HttpResponse
import json
#ici j'importe mes autres vues qui sont dans le dossier others_views, je fais ca pour mieux me retrouver dans le code
from .others_views.dashboard import *
from .others_views.games import *
from .others_views.inscr_conn_decon import *
#ici j'importe mes autres vues qui sont dans le dossier others_views, je fais ca pour mieux me retrouver dans le code
PATH_TO_DICT = "alphabox/json/dict/dictionnary_"

def test(request):
    string = "abcdefghijklmnopqrstuvwxyz"
    for letter in string:
        print('on traite la lettre: '+letter)
        with open(PATH_TO_DICT+letter) as file:
            miniDic = json.load(file)
            newDic = {}
        for word in miniDic :
            print('\t on traite le mot :'+word)
            result = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word) 
            result=str(result.content)
            if result[2]=='[' :
                print("\t \t c'est vaide !")
                pass
            else:
                print("\t\t c'est pas valide ")
                newDic[word] = 1
    
        jsonFile = open(PATH_TO_DICT+letter, "w")
        json.dump(newDic, jsonFile)
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

def quitParty(request):
    #on sauvegarde ses informations en BD
    return index(request)
def error_404(request, exception):
    data = {}
    return render(request,'alphabox/test/test.html', data)