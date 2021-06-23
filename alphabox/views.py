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
        with open(PATH_TO_DICT+letter) as file:
            miniDic = json.load(file)
        for word in miniDic :
            result = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word) 
            result=str(result.content)
            if result[2]=='[' :
                pass
            else:
                del miniDic[word]

        jsonFile = open(PATH_TO_DICT+letter, "w")
        json.dump(miniDic, jsonFile)
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

