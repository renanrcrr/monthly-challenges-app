from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

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

def monthly_challenge_by_number(request, month):
    months = list(month_challenges.keys())
    forward_month = months[month-1]
    if month > 12 or month < 1:
        return HttpResponseNotFound("Invalid month")
    
    return HttpResponseRedirect(f"/challenges/{forward_month}")

def monthly_challenge(request, month):
    return HttpResponse(month_challenges.get(month, "Invalid month"))