# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.shortcuts import render_to_response

from apps.location.serializers import PositionSerializer

from .serializers import ShipSerializer
from .models import Ship


class ShipViewSet(viewsets.ModelViewSet):
    model = Ship
    serializer_class = ShipSerializer
    queryset = Ship.objects.all()


class ShipPositionsView(generics.RetrieveAPIView):
    model = Ship
    serializer_class = PositionSerializer
    queryset = Ship.objects.all()

    def get(self, request, *args, **kwargs):
        ship = self.get_object()
        serializer = self.get_serializer(data=ship.positions.order_by('-created'), many=True)
        serializer.is_valid()
        return Response(serializer.data)


def index(request):
    return render_to_response('index.html')
