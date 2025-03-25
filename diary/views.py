# diary/views.py

from django.shortcuts import render, redirect
from .forms import AffirmationForm
from .models import Affirmation

def index(request):
    if request.method == 'POST':
        form = AffirmationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AffirmationForm()

    affirmations = Affirmation.objects.all().order_by('-date')
    return render(request, 'index.html', {
        'form': form,
        'affirmations': affirmations
    })
