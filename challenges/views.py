from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Dictionary mapping month names to challenge text
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

# View function to handle numeric month input (e.g., /challenges/1/)
def monthly_challenge_by_number(request, month):
    # Convert the keys of the dictionary into a list (i.e., list of months)
    months = list(month_challenges.keys())

    # Check if the month number is outside the valid range (1 to 12)
    if month > 12 or month < 1:
        return HttpResponseNotFound("Invalid month")

    # Get the corresponding month name based on the number (1-based index)
    redirect_month = months[month - 1]

    # Generate the URL for the named route 'month-challenge' with the month name as argument
    reverse_path = reverse("month-challenge", args=[redirect_month])

    # Redirect the user to the appropriate month challenge page
    return HttpResponseRedirect(reverse_path)

# View function to handle textual month input (e.g., /challenges/january/)
def monthly_challenge(request, month):
    # Return the challenge text for the given month or a default error message
    return HttpResponse(month_challenges.get(month, "Invalid month"))
