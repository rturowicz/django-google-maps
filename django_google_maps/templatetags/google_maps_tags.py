# -*- coding: utf-8 -*-
from django import template

from ..settings import GOOGLE_MPAS_DEFAULT_SIZE, GOOGLE_MPAS_DEFAULT_ZOOM


register = template.Library()


@register.inclusion_tag('google_maps/map.html')
def google_map(lat, lng, size, canvas, zoom=GOOGLE_MPAS_DEFAULT_ZOOM):
    mapwh = size.split('x')
    if not len(mapwh) == 2:
        mapwh = GOOGLE_MPAS_DEFAULT_SIZE.split('x')

    return {'lat': lat, 'lng': lng, 'canvas': canvas, 'zoom': zoom, 'width': mapwh[0], 'height': mapwh[1]}
