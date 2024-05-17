from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForms

def rental_review(request):
    if request.method == 'POST':
        form = ReviewForms(request.POST)
        if form.is_valid():  # Corrected: Added parentheses to is_valid
            print(form.cleaned_data)
            return redirect(reverse('rental:thank_you'))

    else:
        form = ReviewForms()       
    return render(request, 'rental/rental_review.html', {'form': form})


def thank_you(request):
    return render(request, 'rental/thank_you.html')
