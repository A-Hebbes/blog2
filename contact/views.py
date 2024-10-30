from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'We have received your message. Thank you')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Something went wrong. Please check the form and submit again.')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})
