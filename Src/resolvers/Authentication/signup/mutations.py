import os
import jwt
import bcrypt
from prisma import Prisma
from graphql import GraphQLError
from helpers.prisma_connect import connect_to_prisma
from datetime import datetime, timedelta, timezone
# from helpers.auth import is_authenticated
# from templates.email_template import html_body
# from templates.send_mail import send_email

prisma = Prisma()
user_exists_error = "User already exists"
user_does_not_exists_error = "User does not exists"
wrong_password = "Wrong Credentials"


class Signup:

    async def signup(self, info, input):
        if await connect_to_prisma(prisma):
            name = input.get('name')
            email = input.get('email')
            password = input.get('password')
            password = password.encode('utf-8')
            user_exists = await prisma.user.find_first(
                where={'email': email}
            )
            if user_exists:
                raise GraphQLError(user_exists_error)

            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            hashed_password = hashed_password.decode()
            
            return await prisma.user.create(
                data={
                    'name': name,
                    'email': email,
                    'password': hashed_password,  # Store the hashed password
                    'created_at': datetime.now()
                }
            )


class Login:

    async def login(self, info, input):
        if await connect_to_prisma(prisma):
            email = input.get('email')
            login_password = input.get('password')
            login_password_byte = login_password.encode('utf-8')

            saved_user = await prisma.user.find_first(
                where={'email': email}
            )
            if not saved_user:
                raise GraphQLError(user_does_not_exists_error)

            login_pass_hash = bcrypt.hashpw(login_password_byte, bcrypt.gensalt())

            passwd = saved_user.password
            hashed = passwd.encode('utf-8')

            payload = {
                "id": saved_user.id,
                "email": email
                }

            # add token expiration time (5 seconds):
            payload["exp"] = datetime.now(tz=timezone.utc) + timedelta(seconds=5)

            if bcrypt.checkpw(login_pass_hash, hashed):
                raise GraphQLError(wrong_password)
            else:
                token = jwt.encode(payload=payload, key=os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))

                # and generate new token
                refresh_token = jwt.encode(payload, "some_secret_phrase", algorithm="HS256")

                return {"message": "Success", "token": token, "refresh_token": refresh_token}
