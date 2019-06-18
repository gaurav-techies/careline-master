# import logging
# import sys
# from jose import jwt
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
#
# from auth0.v3.authentication import Users
# users = Users("carelineapp.au.auth0.com") # Auth0 Domain
#
# user_info = users.userinfo("IL8ddAM2kjhkjhkhjkh1ySXLlkjhkljhkh") # Access Token
# logging.debug(user_info)
#
#
# jwt_token = "evr3336htt4g4tg4rvgr1NiIsImtpZCI6Ik56QkNNalk1TkRZNVFqTTVRVUZHTlRaRVJrUkROMFExUWpNNE4wUkVPVGhHT1RVeVF6TkNNdyJ9.eyJnaXZlbl9uYW1lIjoiU2luYSIsImZhbWlseV9uYW1lIjoiS2FyaW1pIiwibmlja25hbWUiOiJjcmVhbXljb2RlIiwibmFtZSI6IlNpbmEgS2FyaW1pIiwicGljdHVyZSI6Imh0dHBzOi8vcGxhdGZvcm0tbG9va2FzaWRlLmZic2J4LmNvbS9wbGF0Zm9ybS9wcm9maWxlcGljLz9hc2lkPTEwMjEzMTg2Mzc5OTE4Mjg0JmhlaWdodD01MCZ3aWR0aD01MCZleHQ9MTU0MTQ2NjM2OCZoYXNoPUFlUjNGbVlLSTdNVzJldE0iLCJnZW5kZXIiOiJtYWxlIiwibG9jYWxlIjoiZW4tVVMiLCJ1cGRhdGVkX2F0IjoiMjAxOC0xMC0wN1QwMTowNjowOC40MzBaIiwiZW1haWwiOiJjcmVhbXljb2RlQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL3NpbmFrYXJpbWkuYXUuYXV0aDAuY29tLyIsInN1YiI6ImZhY2Vib29rfDEwMjEzMTg2Mzc5OTE4Mjg0IiwiYXVkIjoiNXlkMUM5NHhYSUpseG85ckVwZTVkWURzTXBKdlpTZkMiLCJpYXQiOjE1Mzg4NzQzNjksImV4cCI6MTUzODkxMDM2OX0.ldi4JTszO4EF3kzGdv_L-SCYLzL77RIUw8zCwcHLF9qQcnGAM3dmq1Q-qxNVQKfXW6EeHQshyq6XFpZ2pSI7XUHS_YdtQf_rppmi1eT2u2wU64of0cSx5ZCy28a_KSfKrNNF90jxFWkA48-l9BU32deQza10OGtzojggH48AYGxYy7mrT_xQ4JVgsL8xj6l9Z1yNxX4Q4V6JpqcXTbLyOACpAtrYvPtpmHiNvKxL3jSnaPt4dfL1MaeXXJH-kHtMKxWAoTr6MyaGS8CuI5SOhBaxi7BpwqSuBRbDhRdqaHx6mZHP9CqS3nSqdXhmFKPimORDSfc-z9VRH8goY1oIZQ"
#
#
# secret = """-----BEGIN CERTIFICATE-----
# MIIDCTCCAfGgAwIBAgIJO7s8iLC5jGU9MA0GCSqGSIb3DQEBCwUAMCIxIDAeBgNV
# BAMTF3NpbmFrYXJpbWkuYXUuYXV0aDAuY29tMB4XDTE4MTAwNjAyMDMxOFoXDTMy
# MDYxNDAyMDMxOFowIjEgMB4GA1UEAxMXc2luYWthcmltaS5hdS5hdXRoMC5jb20w
# ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDuhKN5d/jDBEP4GYAnAMfj
# BxSCg/FnTMS6gkznNktM3asyWWr7ii7SMGcrraTO/SV9fqYdE5LX6AWF8KhbxNWo
# qbKJOCqQK33iFo3cM/JHGJHGEvUnKlaQW9zms+MH6r1OxFTAMF/YpLQgWfFz2B9O
# /VLOETzQlvvltsd250oGhXa4yah4LlTQphF8Q7xe7Ci12RDeNXM67cy2AI2cQ43P
# +SQnHzp+Yenn+Awri0AgbnqqJiyTu4EMC6sE8gCmhgD0B+21caVudYRJvzpmkTq5
# l+fX4QAfYD9yMMCwfYpaWXDrtj0VD+mWsyIVlI+q4yH9k0XgHCSvjv6COKbRMoa1
# AgMBAAGjQjBAMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFI/2qbq1NGCUxHkB
# GTwS1G9+hBNDMA4GA1UdDwEB/wQEAwIChDANBgkqhkiG9w0BAQsFAAOCAQEAVpad
# vNhpDvIEXWyhQEjLfdkzjyjUyhB9ZrQPYjPPGuwgmqvkRhbAXh1XLs5aD6NiMSyi
# f4LOTOeRr3xpkSfWTyxhzMWIvLiEkE8Nc/DYEekEtmgNf3OODPkQnB7STS2fKPoD
# WTESNRfu3RRQ7HeXWU4hggGyfSduKJHKHKHJbRklomsB111oDOH0W9QT9CpjoCXN
# NK+so3d6xz5L10ujssIu44wJGpcyvWcw0MLTnNWwCD64hdOHcZusk5xpeL2Lt7pB
# AhydonIqeCzC40rKtMJM+rIxLlgTFMeMK9kjHKKJH+hjkljwHHtucsDGfXXvE7hu
# Q5sz/U3C5EtsLNi/ZA==
# -----END CERTIFICATE-----
# """
# client_id = '97wefw7e8f7wef78ewf7wef78wef78we'
#
# decoded = jwt.decode(jwt_token, secret, algorithms=['RS256'], audience=client_id)

import json
import requests

import jwt
from jwt.algorithms import RSAAlgorithm


class TokenError(Exception):
    pass


class TokenValidator:
    def __init__(self, pass):
        pass

    @property
    def pool_url(self):
        return 'https://careline.au.auth0.com'

    @property
    def _json_web_keys(self):
        response = requests.get(self.pool_url + '/.well-known/jwks.json')
        response.raise_for_status()
        json_data = response.json()

        result = {}
        for item in json_data['keys']:
            result[item['kid']] = item

        return result

    def _get_public_key(self, token):
        headers = jwt.get_unverified_header(token)
        kid = headers['kid']
        jwk_data = self.get_jwt_by_kid(kid)
        return RSAAlgorithm.from_jwk(jwk_data)

    def get_jwt_by_kid(self, kid):
        return json.dumps(self._json_web_keys[kid])

    def validate(self, token):
        public_key = self._get_public_key(token)

        try:
            jwt_data = jwt.decode(
                token,
                public_key,
                issuer=self.pool_url,
                algorithms=['RS256'],
            )
        except (jwt.InvalidTokenError, jwt.ExpiredSignature, jwt.DecodeError) as exc:
            raise TokenError(str(exc))
        return jwt_data