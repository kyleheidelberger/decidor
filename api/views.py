from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def names(request):
    return JsonResponse({'names': ['William', 'Rod', 'Grant']})

