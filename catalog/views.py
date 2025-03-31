from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CookForm, DishSearchForm
from .models import Dish, DishType, Cook


@login_required()
def index(request):
    """View function for the home page of the site."""

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    return render(request, "catalog/index.html")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "catalog/dish.html"
    context_object_name = "dish"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        context["search_form"] = DishSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if self.queryset is None:
            self.queryset = Dish.objects.all()
        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("catalog:dish")
    template_name = "create_form/create_dish.html"

class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("catalog:dish")
    template_name = "create_form/create_dish.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("catalog:dish")
    template_name = "catalog/confirm_delete.html"


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "catalog/dish_type.html"
    context_object_name = "dish_type"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        context["search_form"] = DishSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if self.queryset is None:
            self.queryset = DishType.objects.all()
        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
     model = DishType
     fields = "__all__"
     success_url = reverse_lazy("catalog:dish-type")
     template_name = "create_form/create_dish_type.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
     model = DishType
     fields = "__all__"
     success_url = reverse_lazy("catalog:dish-type")
     template_name = "create_form/create_dish_type.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("catalog:dish-type")
    template_name = "catalog/confirm_delete.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "catalog/cook.html"
    context_object_name = "cook"
    paginate_by = 4


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookForm
    success_url = reverse_lazy("catalog:cook")
    template_name = "create_form/cook_form.html"


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("catalog:cook")
    template_name = "create_form/cook_form.html"


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("catalog:cook")
    template_name = "catalog/confirm_delete.html"


def about_us_view(request: HttpRequest) -> HttpResponse:
    return render(request, "catalog/about_us.html")


def contacts_view(request: HttpRequest) -> HttpResponse:
    return render(request, "catalog/contacts.html")
