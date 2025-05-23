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

def index(request):
    # Generate a list of month names from the dictionary keys
    months = list(month_challenges.keys())

    # Create an HTML response with links to each month's challenge
    response_data = "<h1>Monthly Challenges</h1>"
    response_data += "<p>Click on a month to see the challenge:</p>"

    # Loop through the month names and create links to their respective challenge pages
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        month_capitalize = month.capitalize()
        response_data += f'<a href="{month_path}">{month_capitalize}</a><br>'
    
    # Return the generated HTML as the response
    return HttpResponse(response_data)

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
    challenge_text = month_challenges.get(month, "<h1>Invalid month</h1>")
    response_data = f"<h1>{challenge_text}</h1>"
    # Return the challenge text for the given month or a default error message
    return HttpResponse(response_data)
