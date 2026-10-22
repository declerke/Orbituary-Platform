from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ObituaryForm
from .models import Obituary


def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your remembrance has been shared with the community.')
            return redirect('view_obituaries')
    else:
        form = ObituaryForm()

    return render(request, 'obituaries/obituary_form.html', {'form': form})


def view_obituaries(request):
    obituaries = Obituary.objects.all().order_by('-submission_date', '-pk')
    share_url = request.build_absolute_uri(reverse('view_obituaries'))
    return render(request, 'obituaries/view_obituaries.html', {
        'obituaries': obituaries,
        'share_url': share_url,
    })
