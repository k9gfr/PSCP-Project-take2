from django.shortcuts import render
from django.utils import timezone
import pytz

def time_converter_view(request):
    converted_time = None
    original_time = request.GET.get("time_input")
    target_timezone = request.GET.get("timezone")

    if original_time and target_timezone:
        try:
            naive_time = timezone.datetime.strptime(original_time, "%H:%M")
            aware_time = timezone.make_aware(naive_time, timezone=pytz.timezone("UTC"))
            target_time = aware_time.astimezone(pytz.timezone(target_timezone))
            converted_time = target_time.strftime("%H:%M %p %Z")
        except Exception as e:
            converted_time = f"Error: {str(e)}"

    return render(request, 'time_converter/index.html', {
        'converted_time': converted_time,
        'original_time': original_time,
        'target_timezone': target_timezone
    })
def index(request):
    return render(request, 'time_converter/index.html')
