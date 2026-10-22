from django import forms
from django.utils.text import slugify

from .models import Obituary


class ObituaryForm(forms.ModelForm):
    class Meta:
        model = Obituary
        fields = ('name', 'date_of_birth', 'date_of_death', 'content', 'author')
        labels = {
            'name': 'Person’s name',
            'date_of_birth': 'Date of birth',
            'date_of_death': 'Date of passing',
            'content': 'Their story',
            'author': 'Your name',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'name',
                'aria-describedby': 'name-errors',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'aria-describedby': 'date_of_birth-errors',
            }),
            'date_of_death': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'aria-describedby': 'date_of_death-errors',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 7,
                'aria-describedby': 'content-hint content-errors',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'name',
                'aria-describedby': 'author-errors',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound:
            errors = self.errors
            for name, field in self.fields.items():
                if errors.get(name):
                    field.widget.attrs['aria-invalid'] = 'true'

    def save(self, commit=True):
        obituary = super().save(commit=False)
        base_slug = slugify(obituary.name) or 'memorial'
        candidate = base_slug
        suffix = 2
        existing_slugs = Obituary.objects.all()
        if obituary.pk:
            existing_slugs = existing_slugs.exclude(pk=obituary.pk)

        while existing_slugs.filter(slug=candidate).exists():
            suffix_text = f'-{suffix}'
            candidate = f'{base_slug[:255 - len(suffix_text)].rstrip("-")}{suffix_text}'
            suffix += 1

        obituary.slug = candidate
        if commit:
            obituary.save()
            self.save_m2m()
        return obituary
