#views for the games module
import json
from json.encoder import JSONEncoder
from os import getrandom
from django.http import JsonResponse
from django.core import serializers #pour restructurer des données en format JSOn
from django.http import request
import requests
from django.http.response import HttpResponse
from django.shortcuts import render
import random
from ..models import setting 

# from nltk.corpus import wordnet as wn # pour importer WordNet
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
    return random_entries

def guess_words(request, subModule):
    context = {
        "subModule" : subModule,
        "module" : "guesWords"
    }
    return render(request, 'alphabox/game/guessWords/index.html', context)

#   /game/guessWord/settings
def guess_words_settings(request):
    if request.method == "GET" and request.is_ajax() :
        PARTY_SETTINGS = request.GET
        """PARTY_PATH = "alphabox/json/"+PARTY_SETTINGS["id"]+".json"   #pour stoquer tout ce qui concerne la partie
        jsonFile = open(PARTY_PATH, "w")
        json.dump(PARTY_SETTINGS, jsonFile)
        jsonFile. close()
        """
        with open(PATH_TO_DICT+PARTY_SETTINGS['letter']) as file:
            miniDic = json.load(file)
        return JsonResponse({"dict":miniDic, "randomWords": game_random_words(miniDic)}, status=200)
    else:
        return JsonResponse({"error": "il y a eu un probleme"})

    #return render(request, 'alphabox/game/guessWords/index.html') #par défaut c"esr ca que ca fait 


#   /game/guessWords/find/
def guess_words_findwords(request):
    pass
"""     if request.method == "GET" and request.is_ajax() :
        word =  request.GET['word']
        #on vérifie d'abord que l'utilisateur n'a pas deja entré ce mott en verifiant dans le fichier JSON correspondant
            #en fait on va créer un fichier pour stoquer 
 #       syns = wn.synsets(word)     # recherche des Sysets dans Wordnet
        if (len(syns) != 0):
            return JsonResponse({"found":True, "word":wordToJson(Word(word))}, status=200)
        else:
            return JsonResponse({"found": False}, status=200)
            
        #with open("file.json", "w") as out:
            #data = serializers.serialize("json", request.POST ) 

        #on fait d'autres opértations comme sauver ses réglages en bd, pour l'utilisatteur qui est en ligne
    else:
        return JsonResponse({"error": "vous n'accedez pas coorectemenr à cette URL"})
"""


def wordToJson(word):
    JsonWord = {}
    JsonWord['value'] = word.value
    JsonWord['definition'] = word.definition
    JsonWord['exemples'] = word.example
    JsonWord['POS'] = word.pos
    return JsonWord


"""
# classe pour creer des mots à partir des infos de Wordnet
class Word():
    def __init__(self, name):
        if len(wn.synsets(name)) != 0: #si le mot existe meme d'abord
            self.firstLetter = name[0]
            self.value = name
            self.syns = self.getSyns()
            self.definition = self.setDefinition()
            self.example = self.setExemple()
            self.pos = self.setPOS()  #Part Of Speach
        else: return None

    #donne la définition la plus proche du mot
    def setDefinition(self):
        for syn in wn.synsets(self.value):
            if "01" in syn.name():
                return syn.definition() 
    def setExemple(self):
        for syn in wn.synsets(self.value):
            if "01" in syn.name():
                return syn.examples() 

    def setPOS(self):
        for syn in wn.synsets(self.value):
            if "01" in syn.name():
                if syn.pos() == "v": return "Verb" 
                if syn.pos() == "n": return "Noun" 
                if syn.pos() == "s" or syn.pos() == "a" : return "Adjective" 
                if syn.pos() == "r": return "Adverb" 
    

    def getSyns(self):
        syns = []
        for syn in wn.synsets(self.value):
            names = [self.value] 
            for name in syn.lemma_names():
                if(name not in names):
                    names.insert(len(names), name)
            {}
"""

# section pour le module Learning meaning
def learningMeaning(request):
    context= {
        "module" : "learningMeaning"

    }
    return render(request, 'alphabox/game/learnMeaning/index.html', context)

def usingWords(request):
    context= {
        "module" : "unsingWords"
    }
    return render(request, 'alphabox/game/usingWords/index.html')