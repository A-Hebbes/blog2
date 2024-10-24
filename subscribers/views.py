from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)
                messages.success(request, 'Thank you for subscribing!')
            else:
                messages.error(request, 'You are already subscribed!')
        return redirect('home')
    return render(request, 'subscribers/subscribe.html')

