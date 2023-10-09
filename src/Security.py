import datetime
import pytz
import jwt


class Security():

    timezone = pytz.timezone('America/Bogota')

    @classmethod
    def generate_token(cls, authenticate_user):
        payload = {
            "iat": datetime.datetime.now(tz=cls.timezone),
            "exp": datetime.datetime.now(tz=cls.timezone) + datetime.timedelta(days=1),
            'name': authenticate_user.name,
        }

        return jwt.encode(payload, "clavesecreta", algorithm="HS256")

    @classmethod
    def verify_token(cls, headers):
        if 'Authorization' in headers:
            authorization = headers['Authorization']

            encoded_token = authorization.split(" ")[1][:-1]

            if encoded_token:
                try:
                    jwt.decode(
                        encoded_token, "clavesecreta", algorithms=["HS256"])
                    return True
                except jwt.ExpiredSignatureError:
                    return False
                except jwt.InvalidTokenError:
                    return False

        return False
