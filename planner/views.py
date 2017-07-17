from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView, UpdateView

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
            try:
                weddingHall = WeddingHall.objects.get(wedding=wedding.pk)
                ctx["weddingHall"] = weddingHall
            except:
                pass

            try:
                car = Car.objects.get(wedding=wedding.pk)
                ctx["car"] = car
            except:
                pass

            try:
                photographer = Photographer.objects.get(wedding=wedding.pk)
                ctx["photographer"] = photographer
            except:
                pass

            try:
                band = Band.objects.get(wedding=wedding.pk)
                ctx["band"] = band
            except:
                pass

            try:
                weddingRings = WeddingRings.objects.get(wedding=wedding.pk)
                ctx["weddingRings"] = weddingRings
            except:
                pass

            try:
                alcoholBeverages = AlcoholBeverages.objects.get(wedding=wedding.pk)
                ctx["alcoholBeverages"] = alcoholBeverages
            except:
                pass

            try:
                nonAlcoholBeverages = NonAlcoholBeverages.objects.get(wedding=wedding.pk)
                ctx["nonAlcoholBeverages"] = nonAlcoholBeverages
            except:
                pass

            try:
                church = Church.objects.get(wedding=wedding.pk)
                ctx["church"] = church
            except:
                pass

            try:
                other = Other.objects.get(wedding=wedding.pk)
                ctx["other"] = other
            except:
                pass
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
        wedding = Wedding.objects.get(user=request.user.pk)
        ctx = {"wedding": wedding}
        try:
            weddingHall = WeddingHall.objects.get(wedding=wedding.pk)
            ctx["weddingHall"] = weddingHall
        except:
            pass

        try:
            car = Car.objects.get(wedding=wedding.pk)
            ctx["car"] = car
        except:
            pass

        try:
            photographer = Photographer.objects.get(wedding=wedding.pk)
            ctx["photographer"] = photographer
        except:
            pass

        try:
            band = Band.objects.get(wedding=wedding.pk)
            ctx["band"] = band
        except:
            pass

        try:
            weddingRings = WeddingRings.objects.get(wedding=wedding.pk)
            ctx["weddingRings"] = weddingRings
        except:
            pass

        try:
            alcoholBeverages = AlcoholBeverages.objects.get(wedding=wedding.pk)
            ctx["alcoholBeverages"] = alcoholBeverages
        except:
            pass

        try:
            nonAlcoholBeverages = NonAlcoholBeverages.objects.get(
                wedding=wedding.pk)
            ctx["nonAlcoholBeverages"] = nonAlcoholBeverages
        except:
            pass

        try:
            church = Church.objects.get(wedding=wedding.pk)
            ctx["church"] = church
        except:
            pass

        try:
            other = Other.objects.get(wedding=wedding.pk)
            ctx["other"] = other
        except:
            pass

        return TemplateResponse(request, "wedding.html", ctx)


class WeddingHallUpdateView(UpdateView):
    model = WeddingHall
    fields = "__all__"
    template_name_suffix = "_form_update"
    success_url = "/menu"


class CarUpdateView(UpdateView):
    model = Car
    fields = "__all__"
    template_name_suffix = "_form_update"
    success_url = "/menu"


class PhotographerUpdateView(UpdateView):
    model = Photographer
    fields = "__all__"
    template_name_suffix = "_form_update"
    success_url = "/menu"


class BandUpdateView(UpdateView):
    model = Band
    fields = "__all__"
    template_name_suffix = "_form_update"
    success_url = "/menu"


class WeddingRingsUpdateView(UpdateView):
    model = WeddingRings
    fields = "__all__"
    template_name_suffix = "_form_update"
    success_url = "/menu"


class AlcoholBeveragesUpdateView(UpdateView):
    model = AlcoholBeverages
    fields = "__all__"
    template_name_suffix = "_form_update"
    success_url = "/menu"


class NonAlcoholBeveragesUpdateView(UpdateView):
    model = NonAlcoholBeverages
    fields = "__all__"
    template_name_suffix = "_form_update"
    success_url = "/menu"


class ChurchUpdateView(UpdateView):
    model = Church
    fields = "__all__"
    template_name_suffix = "_form_update"
    success_url = "/menu"


class OtherUpdateView(UpdateView):
    model = Other
    fields = "__all__"
    template_name_suffix = "_form_update"
    success_url = "/menu"
