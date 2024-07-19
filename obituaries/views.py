from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.utils import IntegrityError
import traceback

from .models import Obituary
from .forms import ObituaryForm

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            try:
                print('Form data:', form.cleaned_data)  # Debugging: print form data
                form.save()
                messages.success(request, 'Obituary submitted successfully!')
                return redirect('view_obituaries')  # Redirect to the view that lists all obituaries
            except IntegrityError as e:
                # Log error details to console for debugging
                print('IntegrityError:', str(e))
                print(traceback.format_exc())
                messages.error(request, f'An error occurred: {e}')
        else:
            # Log form errors to console for debugging
           print(f"Form is not valid. Errors: {form.errors.as_json()}")
    else:
        form = ObituaryForm()
    
    return render(request, 'submit_obituary.html', {'form': form})

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})

def home(request):
    return render(request, 'home.html')
