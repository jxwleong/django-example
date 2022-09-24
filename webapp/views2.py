from django.shortcuts import render
from django.http import HttpResponse
from .thread import CreatePatientThread

import random
import logging 

logger = logging.getLogger('django')


def index(request):
    count = 100
    CreatePatientThread(count).start()
    return render(request, 'index.html')