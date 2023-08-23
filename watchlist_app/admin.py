from django.contrib import admin

from watchlist_app.models import Movie


@admin.register(Movie)
class Movie(admin.ModelAdmin):
    pass