from django.shortcuts import render

from .models import Pizza 

def index(request):
    """ the home page for pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    "show all pizzas"
    pizzas= Pizza.objects.order_by('date_added')
    context= {'pizzas':pizzas}
    return render(request,'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    "shows a single pizza and all its toppings"
    pizza= Pizza.objects.get(id=topic_id)
    toppings=pizza.entry_set.order_by('-date_added')
    context= {'pizza': pizza, 'toppings':toppings}
    return render (request, 'pizzas/pizza.html', context)
