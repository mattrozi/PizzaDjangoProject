from django.urls import path

from . import views

app_name='MainApp'

urlpatterns=[

    path('',views.index,name='index'),
    path('Pizzas',views.pizzas,name='Pizzas'),
    path('Pizzas/<int:Pizza_id>/',views.pizza,name='Pizza'),
    #path('new_pizza/',views.new_pizza,name='new_pizza'),
    #path('new_topping/<int:Pizza_id>/',views.new_topping,name='new_topping'),
    #path('edit_topping/<int:topping_id>/',views.edit_topping,name='edit_topping'),
    path('new_comment/<int:Pizza_id>/',views.new_comment, name='new_comment'),
]