from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect
import json

# Create your views here.
from .forms import selectMapForm
from achillea_utils import prepare_map

def index(request): 
    return render(request, 'contproc/index.html')

def map_view(request):
    if request.method == "POST":
        form = selectMapForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("maps").id
            plotly_map = prepare_map(id)
            form = selectMapForm()
            form.fields['maps'].initial = id
            return render(request, "contproc/map.html", {
                "form": form,
                "plotly_map": json.dumps(plotly_map),
            })
    return render(request, "contproc/map.html", {
        "form": selectMapForm(),
        "plotly_map": json.dumps({})
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "contproc/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "contproc/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
