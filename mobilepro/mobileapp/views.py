from django.shortcuts import render
from django.http import JsonResponse
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def mob(request):
    if request.method == "POST":
        number = request.POST.get('phone_number', '')
        try:
            # Parsing String to the Phone number
            phoneNumber = phonenumbers.parse(number)

            # Getting timezone
            timeZone = timezone.time_zones_for_number(phoneNumber)

            # Getting geolocation
            geolocation = geocoder.description_for_number(phoneNumber, "en")

            # Getting service provider
            service = carrier.name_for_number(phoneNumber, "en")

            # Preparing response data
            data = {
                'timezone': str(timeZone),
                'location': geolocation,
                'service_provider': service
            }
            return JsonResponse(data)

        except phonenumbers.NumberParseException:
            return JsonResponse({'error': 'Invalid phone number format.'}, status=400)

    return render(request, 'phone_info.html')
