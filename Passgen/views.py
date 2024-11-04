from django.shortcuts import render, HttpResponse
import random
from django.http import JsonResponse

# Create your views here.
def home(request):
    # return HttpResponse('<h3>Edit the url and add \'/password_gen\' to get the pass phrase.</h3>')
    return render(request, 'home.html')


def PasswdGenerator(request):
    LowercaseCharacters = 'abcdefghijklmnopqrstuvwxyz'
    UppercaseCharacters = LowercaseCharacters.upper()
    Numbers = '123456789'
    SpecialCharacters = '!@#$%^&*()_+[]{}:;,./?-'
    # CharacterSet = list(LowercaseCharacters + UppercaseCharacters + Numbers + SpecialCharacters)
    CharacterSet = list(LowercaseCharacters)
    if request.GET.get('uppercase'):
        CharacterSet.extend(list(UppercaseCharacters))

    if request.GET.get('digits'):
        CharacterSet.extend(list(Numbers))

    if request.GET.get('specialcharacters'):
        CharacterSet.extend(list(SpecialCharacters))

    length = int(request.GET.get('length', 8))
    
    Passkey = ''
    for x in range(length):
        Passkey += random.choice(CharacterSet)
    # pas = {'Passkey': Passkey}

    return render(request, 'password.html', {'Passkey': Passkey})