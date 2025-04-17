from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    month_challenges = {
        "january": "January Challenge",
        "february": "February Challenge",
        "march": "March Challenge",
        "april": "April Challenge",
        "may": "May Challenge",
        "june": "June Challenge",
        "july": "July Challenge",
        "august": "August Challenge",
        "september": "September Challenge",
        "october": "October Challenge",
        "november": "November Challenge",
        "december": "December Challenge",
    }
    return HttpResponse(month_challenges.get(month, "Invalid month"))