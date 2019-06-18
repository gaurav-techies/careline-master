from django.conf import settings
import requests


def shorten_url(long_url):
     bitly_url = "https://api-ssl.bitly.com/v4/shorten"
     body = {"long_url": long_url}
     header = {"Authorization": "Bearer {}".format(settings.BITLY_ACCESS_TOKEN)}
     short_url = requests.post(bitly_url, headers=header, json=body)
     return short_url.body['link']
     print(long_url)
     print(bitly_url)