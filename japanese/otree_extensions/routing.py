from django.conf.urls import url
from ..consumers import AuctionRoom
from otree.channels.routing import websocket_routes


websocket_routes += [
    url(r'^japanese/(?P<params>[\w,]+)/$',
        AuctionRoom),
]
