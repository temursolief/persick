from django.urls import path
from .views import payment_process, payment_completed, payment_canceled
from .webhooks import stripe_webhook

app_name = 'payment'


urlpatterns = [
    path('process/', payment_process, name='process'),
    path('completed/', payment_completed, name='completed'),
    path('canceled/', payment_canceled, name='canceled'),
    path('webhook/', stripe_webhook, name='stripe-webhook'),
]