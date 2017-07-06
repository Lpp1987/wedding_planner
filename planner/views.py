from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView

from planner.models import *


class BaseView(View):

    def get(self, request):
        return TemplateResponse(request, "base.html")


class MenuView(View):

    def get(self, request):
        return TemplateResponse(request, "menu.html")


class WeddingHallCreateView(CreateView):
    model = WeddingHall
    fields = "__all__"
    success_url = "/menu"
