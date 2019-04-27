from random import random, randint
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.gis.geos import Point

from .models import Ship


def create_positions(ship):
    lat = 19.99
    long = 73.78
    time = timezone.now() - timedelta(days=1)

    # Create 20 locations, 5 mins apart
    for _ in range(0, 20):
        add_lat = random() / 100
        add_lon = random() / 100
        point = Point(x=long+add_lon, y=lat+add_lat)
        ship.positions.create(location=point, created=time)
        time += timedelta(minutes=5)


def create_ship(name):
    imo = int(''.join(["%s" % randint(0, 9) for _ in range(0, 7)]))
    ship = Ship.objects.create(name=name, imo=imo)
    create_positions(ship)
    return ship


class ShipModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        create_ship('test ship')

    def test_imo_label(self):
        ship = Ship.objects.last()
        field_label = ship._meta.get_field('imo').verbose_name
        self.assertEquals(field_label, 'imo')

    def test_name_label(self):
        ship = Ship.objects.last()
        field_label = ship._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')


class ShipViewTests(TestCase):

    def test_ships_endpoint_status(self):
        """ Tests that api/ships/ returns a 200 """

        response = self.client.get(reverse('ships-list'))
        self.assertEqual(response.status_code, 200)

    def test_ship_location_endpoint_status(self):
        """ Tests that api/ships/location returns a 200 """

        ship = create_ship(name='test_ship')
        response = self.client.get(reverse('ship-positions', args=[ship.imo,]))
        self.assertEqual(response.status_code, 200)

    def test_ship_locations(self):
        """ Checks that the positions are correct aswell as the ordering """

        ship = create_ship(name='test_ship')
        response = self.client.get(reverse('ship-positions', args=[ship.imo, ]))
        positions = ship.positions.order_by('-created')

        for position_one, position_two in zip(response.data, positions):
            self.assertEqual(position_one['date'], position_two.date)
            self.assertEqual(position_one['time'], position_two.time)

    def test_amount_of_ship_locations(self):
        ship = create_ship(name='test_ship')
        response = self.client.get(reverse('ship-positions', args=[ship.imo, ]))
        self.assertEqual(len(response.data), 20)

    def test_index_endpoint_status(self):
        """ Checks the endpoint for mapping the positions for ships"""

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
