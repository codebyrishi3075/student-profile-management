from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def homepage(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'base.html', {'messgae': 'Welcome To Student Profile Management System'})