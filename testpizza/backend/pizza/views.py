from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pizza, Topping
from .forms import PizzaForm
from django.views.generic import ListView, CreateView
from django.db.models import Q
from django.urls import reverse


def index(request):

    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas,
        'title': 'Список пицц',
        'pizza_form': PizzaForm
    }
    return render(request, 'pizza/index.html', context)


def pizza(request, slug):
    p = get_object_or_404(Pizza, slug=slug)
    context = {
        "pizza": p,
    }
    return render(request, 'pizza/pizza.html', context)


@login_required(login_url='/')
def create_pizza(request):
    if request.method == 'POST':
        post = request.POST.copy()
        post['created_by'] = request.user.id
        pizza_form = PizzaForm(post, request.FILES, initial={'created_by': request.user.id})
        if pizza_form.is_valid():
            pizza_form.save()
            return redirect('/pizza')
        else:
            pass  # Обработчик ошибок
    else:
        pizza_form = PizzaForm()
    context = {
        'pizza_form': pizza_form
    }
    return render(request, 'pizza/create_pizza.html', context)

# class CreatePizza(CreateView):
#     model = Pizza
#     form_class = PizzaForm
#     extra_context = {'pizzas': Pizza.objects.all()}
#     template_name = 'pizza/create_pizza.html'
#     success_url = '/pizza'

    # def get_success_url(self):
    #     return reverse('create_pizza', kwargs={'pizza_slug': self.object.pizza_slug})


class SearchResultView(ListView):
    model = Pizza
    template_name = 'pizza/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Pizza.objects.filter(
            Q(toppings__name__icontains=query) | Q(name__icontains=query)
        )
        return object_list
