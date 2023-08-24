from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

'''
class Movie(models.Model):
    MAX_MOVIE_NAME_LEN = 50
    MAX_MOVIE_DESCRIPTION_LEN = 200
    name = models.CharField(
        max_length=MAX_MOVIE_NAME_LEN,
    )
    description = models.CharField(
        max_length=MAX_MOVIE_DESCRIPTION_LEN,
    )
    active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name
        
'''


class StreamPlatform(models.Model):
    NAME_MAX_LEN = 30
    ABOUT_MAX_LEN = 150
    WEBSITE_MAX_LEN = 200
    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )
    about = models.CharField(
        max_length=ABOUT_MAX_LEN,
    )
    website = models.URLField(
        max_length=WEBSITE_MAX_LEN,
    )

    def __str__(self):
        return self.name


class WatchList(models.Model):
    TITLE_MAX_LEN = 50
    STORYLINE_MAX_LEN = 200
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    storyline = models.CharField(
        max_length=STORYLINE_MAX_LEN,
    )
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(
        default=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    DESCRIPTION_MAX_LEN = 200
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    active = models.BooleanField(
        default=True,
    )
    description = models.CharField(
        max_length=DESCRIPTION_MAX_LEN,
        null=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    update = models.DateTimeField(
        auto_now=True,
    )
    watchlist = models.ForeignKey(
        WatchList,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    def __str__(self):
        return str(self.rating) + ' ' + self.watchlist.title
