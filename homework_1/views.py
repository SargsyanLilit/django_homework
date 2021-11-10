from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime


def greeting(request):
    return HttpResponse("Welcome to django homework_1 app!")


def introduction(request):
    return HttpResponse("Information about the project!")


def current_date_time(request):
    return HttpResponse(f"Current date and time is: {datetime.now()}")


def square_of_number_dictionary(request):
    my_dict = {i: i*i for i in range(1,16)}
    return HttpResponse(f"{my_dict}")






