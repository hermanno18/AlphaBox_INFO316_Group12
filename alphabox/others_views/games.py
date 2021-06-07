from django.http import request
from django.shortcuts import render

def guess_words(request):
    return render(request, 'alphabox/game/guessWords/index.html')