from django.db import models


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
