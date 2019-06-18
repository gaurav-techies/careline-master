import os
from jose import jwt

private_key = os.environ.get('CREATE_JWT_PRIVATE')
public_key = os.environ.get('CREATE_JWT_PUBLIC')
kid = {'kid': 'MUQzNTVBREU1ODdGNDdBNzJGQUM3NzY0QjcxODNFOUJGREI0QTQ0NQ'}

payload = {
      "user_id": "5bbf096208b2db2fcfe9be49",
      "email": "matt.millen@netteky.com",
      "email_verified": False,
      "sid": "VLbaBHm4Tflk0-ig3WpOEJ3qK8QDo-Ec",
      "jti": "5bbf0c2c79d5f43aaa8d9060",
      "iat": 1539247149,
      "exp": 1539247209,
      "aud": "urn:auth0:careline:Username-Password-Authentication",
      "iss": "urn:auth0"
    }
token = jwt.encode(payload, private_key, algorithm='RS256', headers=kid)

print(token)