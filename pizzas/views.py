from django.shortcuts import render

def index(request):
    """ the home page for pizzeria"""
    return render(request, 'pizzas/index.html')
