from django.urls import path

from . import views

# URL patterns for the "challenges" app
urlpatterns = [
    # Route to handle numeric month input (e.g., /challenges/1, /challenges/12)
    # This will call the 'monthly_challenge_by_number' view and pass the number as an integer
    path("<int:month>", views.monthly_challenge_by_number),
    
    # Route to handle string-based month input (e.g., /challenges/january, /challenges/december)
    # This will call the 'monthly_challenge' view and pass the month name as a string
    # The 'name' attribute is used to reference this route elsewhere in the project (e.g., with 'reverse')
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
