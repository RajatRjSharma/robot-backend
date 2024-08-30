from .base import *


DEBUG = False
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "13.127.133.231",
    "ec2-13-127-133-231.ap-south-1.compute.amazonaws.com",
]
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://ec2-13-127-133-231.ap-south-1.compute.amazonaws.com",
]
