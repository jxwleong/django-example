# Ref: https://www.youtube.com/watch?v=U5nuICIuAp0&ab_channel=CodeKeen
import threading
import logging
import random 
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

logger = logging.getLogger('django')

class CreatePatientThread(threading.Thread):
    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)

    def run(self):
        try:
            logger.info("Thread execution started!")
            
            for i in range(self.total):
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
        except Exception as e:
            logger.exception(e)
