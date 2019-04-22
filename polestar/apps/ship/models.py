from django.db import models


class Ship(models.Model):
    imo = models.PositiveIntegerField(primary_key=True)
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name
