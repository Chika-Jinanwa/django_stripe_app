from django.shortcuts import render, redirect
from .models import Product
from django.urls import reverse
import stripe_app
import logging
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import (
    HttpResponse,
    HttpResponseRedirect
)
from django.conf import settings
from django.http import JsonResponse
import stripe


stripe.api_key = 'sk_test_YfHv3HSc5zexgdepinZcvPlG00uxYjQKIM'
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')

@login_required
def charge(request):
    amount = 49.99
    if request.method == 'POST':
        print('Data:', request.POST)
    customer=stripe.Customer.create(
        name=request.POST['name'],
        email=request.POST['email'],
        source=request.POST['stripeToken']
    )
    subscription= stripe.Subscription.create(
        customer = customer,
        items=[{'plan':'plan_HEV1zEtTkw6zNi'}],
        trial_end = 1592352000,
   
    )
    cancel_subscription = stripe.Subscription.delete(
        "sub_HFIWEVRqc15tZg"
    )

    return redirect(reverse('success', args=[amount]))

@login_required
def successMsg(request, args):
    amount = args
    return render(request, 'success.html', {'amount': amount})
