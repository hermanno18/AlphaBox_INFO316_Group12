#views for the games module
import json
from json.encoder import JSONEncoder
from django.http import JsonResponse
from django.core import serializers #pour restructurer des données en format JSOn
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from ..models import setting
from nltk.corpus import wordnet as wn


def guess_words(request):
    return render(request, 'alphabox/game/guessWords/index.html')

#   /game/guessWord/settings
def guess_words_settings(request):
    
    if request.method == "GET" and request.is_ajax() :
        PARTY_SETTINGS = request.GET
        PARTY_PATH = "alphabox/json/"+PARTY_SETTINGS["id"]+".json"   #pour stoquer tout ce qui concerne la partie
        jsonFile = open(PARTY_PATH, "w")
        json.dump(PARTY_SETTINGS, jsonFile)
        jsonFile. close()
        word = Word('good')

        return JsonResponse({"je retourne : ": 'ss'}, status=200)
    else:
        return JsonResponse({"error": "il y a eu un probleme"})

    #return render(request, 'alphabox/game/guessWords/index.html') #par défaut c"esr ca que ca fait 

#   /game/guessWords/find/
def guess_words_findwords(request):
    if request.method == "GET" and request.is_ajax() :
        word =  request.GET['word']
        #on vérifie d'abord que l'utilisateur n'a pas deja entré ce mott en verifiant dans le fichier JSON correspondant
            #en fait on va créer un fichier pour stoquer 
        syns = wn.synsets(word)
        if (len(syns) != 0):
            return JsonResponse({"found":True, "word":wordToJson(Word(word))}, status=200)
        else:
            return JsonResponse({"found": False}, status=200)
            
        #with open("file.json", "w") as out:
            #data = serializers.serialize("json", request.POST ) 

        #on fait d'autres opértations comme sauver ses réglages en bd, pour l'utilisatteur qui est en ligne
    else:
        return JsonResponse({"error": "vous n'accedez pas coorectemenr à cette URL"})



def wordToJson(word):
    JsonWord = {}
    JsonWord['value'] = word.value
    JsonWord['definition'] = word.definition
    JsonWord['exemples'] = word.example
    JsonWord['POS'] = word.pos
    return JsonWord

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

    """donne la définition la plus proche du mot"""
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
