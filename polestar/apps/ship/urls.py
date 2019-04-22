from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('ships', views.ShipViewSet, base_name='ships')

urlpatterns = [
    url('api/', include(router.urls)),
    url('api/positions/(?P<pk>[\d]+)/', views.ShipPositionsView.as_view(), name='ship-positions')
]