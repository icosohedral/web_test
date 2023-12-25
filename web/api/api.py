from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests, os, json, shutil, time, base64

def cprint(text, color='green', bold=True, underline=False):
    normal = '\033[0m'
    styles = {
        'bold': '\033[1m',
        'underline': '\033[4m'
    }
    colors = {
    'pink': '\033[95m',
    'blue': '\033[94m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m', 
    }
    if bold:
        text = styles['bold'] + text
    if underline:
        text = styles['underline'] + text
    if color:
        text = colors[color] + text
    print(text+normal)
    
def test(request):
    return render(request, 'api.html', {'text':'salut!'})
    
if __name__ == '__main__':
    pass
