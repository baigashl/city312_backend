import requests
from django.http import JsonResponse

from city312_backend import settings


def verify_recaptcha(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('captcha')
        secret_key = settings.DRF_RECAPTCHA_SECRET_KEY
        verify_url = f"https://www.google.com/recaptcha/api/siteverify?secret={secret_key}&response={recaptcha_response}"

        response = requests.get(verify_url)
        response_json = response.json()

        if response_json['success']:
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failed'})
