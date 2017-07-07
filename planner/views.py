from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from planner.models import *


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/menu")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


class BaseView(View):

    def get(self, request):
        return TemplateResponse(request, "base.html")


class MenuView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("/")
        try:
            wedding = Wedding.objects.get(user=request.user.pk)
            ctx = {"wedding": wedding}
        except:
            ctx = {"wedding": "NO-WEDDING"}
        return TemplateResponse(request, "menu.html", ctx)


class WeddingHallCreateView(CreateView):
    model = WeddingHall
    fields = "__all__"
    success_url = "/menu"


class CarCreateView(CreateView):
    model = Car
    fields = "__all__"
    success_url = "/menu"


class PhotographerCreateView(CreateView):
    model = Photographer
    fields = "__all__"
    success_url = "/menu"


class BandCreateView(CreateView):
    model = Band
    fields = "__all__"
    success_url = "/menu"


class WeddingRingsCreateView(CreateView):
    model = WeddingRings
    fields = "__all__"
    success_url = "/menu"


class AlcoholBeveragesCreateView(CreateView):
    model = AlcoholBeverages
    fields = "__all__"
    success_url = "/menu"


class NonAlcoholBeveragesCreateView(CreateView):
    model = NonAlcoholBeverages
    fields = "__all__"
    success_url = "/menu"


class ChurchCreateView(CreateView):
    model = Church
    fields = "__all__"
    success_url = "/menu"


class OtherCreateView(CreateView):
    model = Other
    fields = "__all__"
    success_url = "/menu"


class WeddingCreateView(CreateView):
    model = Wedding
    fields = "__all__"
    success_url = "/menu"


class WeddingView(View):

    def get(self, request):
        user = request.user.id
        wedding = Wedding.objects.get(user=user)
        ctx = {"wedding": wedding}
        return TemplateResponse(request, "wedding.html", ctx)