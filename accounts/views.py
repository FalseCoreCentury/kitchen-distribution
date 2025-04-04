from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request: HttpRequest) -> None | HttpResponse | HttpResponseRedirect:
    if request.method == "GET":
        return render(request, "accounts/login.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(f"Method: {request.method}")
        print(f"POST data: {request.POST}")
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("catalog:index"))

        error_context = {"error": "Invalid info"}
        return render(request, "accounts/login.html", context=error_context)


def logout_view(request: HttpRequest) -> None | HttpResponse | HttpResponseRedirect:
    logout(request)
    return render(request, "accounts/log_out.html")
