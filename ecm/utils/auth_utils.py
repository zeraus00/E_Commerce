from datetime import datetime, timezone, timedelta

from jose import jwt

from passlib.context import CryptContext

from ecm.config.settings import Settings

crypt_context = CryptContext(schemes=['argon2'], deprecated='auto')
settings = Settings()


class AuthUtils:

    @staticmethod
    def hash_password(plain_password: str):
        return crypt_context.hash(plain_password)

    @staticmethod
    def verify_hashed_password(plain_password, hashed_password):
        return crypt_context.verify(secret=plain_password, hash=hashed_password)

    @staticmethod
    def authenticate_user(data: dict, plain_password: str):
        try:
            if not AuthUtils.verify_hashed_password(
                    plain_password=plain_password,
                    hashed_password=data['password']):
                return False
            return True
        except Exception as e:
            print(f'An error occurred {e}')
            return False

    @staticmethod
    def generate_access_token(data: dict):
        to_encode = data.copy()
        expires = datetime.now(timezone.utc) + timedelta(minutes=30)

        to_encode.update({'exp': expires})
        payload = jwt.encode(to_encode, settings.JWT_KEY, algorithm=settings.JWT_ALGORITHM)
        return payload