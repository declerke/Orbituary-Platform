from django.shortcuts import render, redirect
from django.utils.text import slugify
from .obituaries import Obituary
from django.urls import reverse

def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']
        slug = slugify(name)
        
        obituary = Obituary(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author,
            slug=slug
        )
        obituary.save()
        return redirect(reverse('view_obituaries'))
    return render(request, 'obituaries/obituary_form.html')

def view_obituaries(request):
    obituaries = Obituary.objects.all().order_by('-submission_date')
    return render(request, 'obituaries/view_obituaries.html', {'obituaries': obituaries})
