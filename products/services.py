import stripe
from django.http import Http404
from django.urls import reverse
from django.conf import settings

from products.models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


def get_product_by_id(id):
    try:
        return Item.objects.get(id=id)
    except Item.DoesNotExist:
        return ''


def create_checkout_session(product, domain):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': product.price,
                    'product_data': {
                        'name': product.name
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=domain + '/success/',
        cancel_url=domain + '/cancel/',
    )
    return checkout_session