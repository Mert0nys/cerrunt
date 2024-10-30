from django.contrib import admin
from django.urls import path
from currency_app.views import CurrentUSDRate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-current-usd/', CurrentUSDRate.as_view(), name='current_usd_rate'),
]