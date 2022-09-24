from django.shortcuts import render
from django.http import HttpResponse
import random
import logging 

logger = logging.getLogger('django')

from .models import Patient
from faker import Faker
from faker.providers import DynamicProvider

fake = Faker()
status_provider = DynamicProvider(
    provider_name='status',
    elements = ['positive', 'negative']
)
state_provider = DynamicProvider(
    provider_name='state',
    elements = ['Pulau Pinang', 'Kuala Lumpur', 'Selangor', 'Kuantan']
)

city_provider = DynamicProvider(
    provider_name='city',
    elements = ['City A', 'City B', 'City C', 'City D']
)


fake.add_provider(status_provider)
fake.add_provider(state_provider)
fake.add_provider(city_provider)
# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')

def index(request):
    count = 100

    for i in range(count):
        logger.info(f'Patient {i}')
        Patient.objects.create(
            name = fake.name(),
            ic = random.randint(10000000, 90000000),
            status = fake.status(),
            date = fake.date_time(),
            street_address = fake.address(),
            postcode = random.randint(10000, 20000),
            city = fake.city(),
            state = fake.state()
        )
    try:
        raise Exception("Failed to connect to database")
    except Exception as e:
        logger.exception(e)


    return render(request, 'index.html')