from django.shortcuts import render,redirect

from .forms import CommentForm, PizzaForm, ToppingForm

from .models import Pizza,Topping

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'MainApp/index.html')

@login_required
def pizzas(request):
    Options=Pizza.objects.all()

    context={'pizzas':Options}

    return render(request,'MainApp/Pizzas.html',context)

@login_required
def pizza(request,Pizza_id):
    pizza=Pizza.objects.get(id=Pizza_id)
    toppings=pizza.topping_set.order_by('-date_added')
    comments=pizza.comment_set.order_by('-date_added')

    context={'Pizza':pizza,'Toppings':toppings,'comments':comments}

    return render(request,'MainApp/Pizza.html',context)

@login_required
def new_pizza(request):

    if request.method!='POST':
        form=PizzaForm()
    else:
        form=PizzaForm(data=request.POST)

        if form.is_valid():
            new_pizza=form.save()

            return redirect('MainApp:Pizzas')

    context={'form':form}
    return render(request,'MainApp/new_pizza.html',context)


@login_required
def new_topping(request,Pizza_id):
    pizza=Pizza.objects.get(id=Pizza_id)

    if request.method!='POST':
        form=ToppingForm()
    else:
        form=ToppingForm(data=request.POST)

        if form.is_valid():
            new_topping=form.save(commit=False)
            new_topping.pizza=pizza
            new_topping.save()
            return redirect('MainApp:Pizza',Pizza_id=Pizza_id)

    context={'form':form, 'Pizza':pizza}
    return render(request,'MainApp/new_topping.html',context)

@login_required
def edit_topping(request,topping_id):
    topping=Topping.objects.get(id=topping_id)
    pizza=topping.pizza


    if request.method!='POST':
        form=ToppingForm(instance=topping)
    else:
        form=ToppingForm(instance=topping,data=request.POST)

        if form.is_valid():
            new_topping=form.save(commit=False)
            new_topping.pizza=pizza
            new_topping.save()
            return redirect('MainApp:Pizza',Pizza_id=pizza.id)

    context={'form':form, 'Pizza':pizza, 'topping':topping}
    return render(request,'MainApp/edit_topping.html',context)

@login_required
def new_comment(request,Pizza_id):
    pizza=Pizza.objects.get(id=Pizza_id)

    if request.method!='POST':
        form=CommentForm()
    else:
        form=CommentForm(data=request.POST)

        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.pizza=pizza
            new_comment.save()
            return redirect('MainApp:Pizza',Pizza_id=Pizza_id)

    context={'form':form, 'Pizza':pizza}
    return render(request,'MainApp/new_comment.html',context)




