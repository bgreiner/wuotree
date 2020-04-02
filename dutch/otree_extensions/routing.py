from django.conf.urls import url
from ..consumers import AuctionRoom
from otree.channels.routing import websocket_routes


websocket_routes += [
    url(r'^dutch/(?P<params>[\w,]+)/$',
        AuctionRoom),
]
