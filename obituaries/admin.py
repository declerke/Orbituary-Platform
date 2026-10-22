from django.contrib import admin

from .models import Obituary


@admin.register(Obituary)
class ObituaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'date_of_death', 'author', 'submission_date')
    list_filter = ('submission_date',)
    search_fields = ('name', 'content', 'author')
    ordering = ('-submission_date', 'name')
