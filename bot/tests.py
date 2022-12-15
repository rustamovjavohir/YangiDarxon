import requests
from django.test import TestCase


# Create your tests here.
def send_req():
    response = requests.get(url="https://api.rustamovdev.uz/")
    print(response.json())


if __name__ == '__main__':
    send_req()
