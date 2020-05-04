from django.shortcuts import render, redirect 

from .models import Pizza, topping
from .forms import new_commentForm 

def index(request):
    """ The home page for pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    "show all pizzas"
    pizzas= Pizza.objects.order_by('date_added')
    context= {'pizzas':pizzas}
    return render(request,'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    "shows a single pizza and all its toppings"
    Pizzas= Pizza.objects.get(id=pizza_id)
    toppings=Pizzas.topping_set.order_by('-date_added')
    context= {'Pizzas': Pizzas, 'toppings':toppings}
    return render (request, 'pizzas/pizza.html', context)

def new_comment(request, pizza_id):
      
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = new_commentForm()
    else:
        form = new_commentForm(data=request.POST)
        if form.is_valid():
            new_Comment = form.save(commit=False)
            new_Comment.pizza = pizza
            new_Comment.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

       # Display a blank or invalid form.
    context = {'pizza': pizza, 'form': form}
    return render(request, 'pizzas/new_comment.html', context)