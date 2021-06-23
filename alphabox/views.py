from django.shortcuts import render
from django.http import HttpResponse

#ici j'importe mes autres vues qui sont dans le dossier others_views, je fais ca pour mieux me retrouver dans le code
from .others_views.dashboard import *
from .others_views.games import *
from .others_views.inscr_conn_decon import *
#ici j'importe mes autres vues qui sont dans le dossier others_views, je fais ca pour mieux me retrouver dans le code
PATH_TO_DICT = "alphabox/json/dict/dictionnary_"

def game_random_words(dic):
    entry_list = list(dic.items())
    random_entries = []
    i = 0
    while i < 5:
        rand = random.choice(entry_list)[0]

        if (rand not in random_entries):
            result = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+rand) 
            result=str(result.content)
            if result[2]=='[' :
                random_entries.append(rand)
                i+=1
            else:
                del diction[]
    
    return random_entries

def test(request):
    string = "abcdefghijklmnopqrstuvwxyz"
    for letter in string:
        with open(PATH_TO_DICT+PARTY_SETTINGS['letter']) as file:
            miniDic = json.load(file)

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

