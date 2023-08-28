from datetime import datetime
from functools import wraps

from prisma import Prisma

from helpers.prisma_connect import connect_to_prisma
# from flask import request

prisma = Prisma()

def custom_decorator(route_function):
    @wraps(route_function)
    def decorator(*args, **kwargs):
        # Add your decorator logic here before the route function is called
        print("Decorator logic before handling the request")
        response = route_function(*args, **kwargs)
        # Add any post-processing logic here
        return response
    return decorator



async def audit_log(self, info, input):
    if await connect_to_prisma(prisma):
        userId = input.get("userId")

        details = "Create"

        return await prisma.audit_log.create(
            data={
                "timestamp": datetime.now(),
                "userId": userId,
                "details": details
            }
        )