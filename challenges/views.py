from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge_by_number(request, month):
    month_challenges = {
        1: "January Challenge",
        2: "February Challenge",
        3: "March Challenge",
        4: "April Challenge",
        5: "May Challenge",
        6: "June Challenge",
        7: "July Challenge",
        8: "August Challenge",
        9: "September Challenge",
        10: "October Challenge",
        11: "November Challenge",
        12: "December Challenge",
    }
    if month > 12 or month < 1:
        return HttpResponseNotFound("Invalid month")
    else:
        challenge_text = month_challenges[month]
        return HttpResponse(challenge_text)

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