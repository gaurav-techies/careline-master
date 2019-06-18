from django.template import Library
from django.conf import settings
import random
import time
register = Library()


@register.simple_tag
def website_domain():
    return settings.WEBSITE_DOMAIN

@register.simple_tag
def google_maps():
    return settings.MAPS_API

@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter
def fraction(number):
    out = []
    finals = number.split(".")
    for x in range(int(finals[0])):
        out.append([1, x])

    if len(finals)>1:
        out.append([0, 1])

    return out

@register.simple_tag
def tickref():
        rng = random.SystemRandom(45645 * time.time())
        ticket_ref = [str(rng.randint(0, 9)) for i in range(10)]
        ticket_ref = ''.join(ticket_ref)

        return ticket_ref