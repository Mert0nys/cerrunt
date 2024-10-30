import requests
import time
from django.http import JsonResponse
from django.views import View
from .models import CurrencyRequest

class CurrentUSDRate(View):
    def get(self, request):
        # Пауза между запросами
        time.sleep(10)

        # Получение курса доллара к рублю из внешнего API
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        usd_to_rub = data['rates']['RUB']

        # Сохранение запроса в базу данных
        currency_request = CurrencyRequest(usd_to_rub_rate=usd_to_rub)
        currency_request.save()

        # Получение последних 10 запросов
        last_requests = CurrencyRequest.objects.order_by('-timestamp')[:10]

        return JsonResponse({
            'current_usd_to_rub': usd_to_rub,
            'last_requests': [
                {
                    'timestamp': req.timestamp,
                    'usd_to_rub_rate': str(req.usd_to_rub_rate)
                } for req in last_requests
            ]
        })
