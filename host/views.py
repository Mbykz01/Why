from django.http import JsonResponse, HttpResponse
from datetime import datetime
import pytz

def get_info(request):
    # Get query parameters from the request
    slack_name = request.GET.get('slack_name', 'Abdulkarim Ibrahim Aminu')
    track = request.GET.get('track', 'backend')

    # Get the current day of the week
    current_day = datetime.now(pytz.utc).strftime('%A')

    # Get the current UTC time
    current_utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub repository URLs
    github_file_url = f"{github_repo_url}/why/blob/main/host/views.py"
    github_repo_url = "https://github.com/Mbykz01/why"

    # Prepare the response data
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }

    # Return the response in JSON format
    response = JsonResponse(response_data)

    # Set the content type to JSON
    response['Content-Type'] = 'application/json'

    # Return the JSON response
    return response

def root_view(request):
    return HttpResponse("Welcome to the root URL of the application.")
