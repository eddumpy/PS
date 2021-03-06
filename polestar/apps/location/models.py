from django.contrib.gis.db import models


class Position(models.Model):
    location = models.PointField()
    created = models.DateTimeField()
    ship = models.ForeignKey('ship.Ship', on_delete=models.CASCADE, related_name='positions')

    def __str__(self):
        return "{}, {}".format(self.latitude, self.longitude)

    @property
    def longitude(self):
        return self.location.x if self.location else None

    @property
    def latitude(self):
        return self.location.y if self.location else None

    @property
    def time(self):
        return self.created.time() if self.created else None

    @property
    def date(self):
        return self.created.date() if self.created else None
