import os,django,sys
from utils.inner import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestAutomation.settings')
django.setup()
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
import pytest
import requests
import traceback
from product_manage.models import Product,Notifier,Modular
from testcase_manage.models import TestCase
from django.forms.models import model_to_dict
import time
import json
import re
import pytest

with open("case.py",encoding='utf-8') as f:
    con = f.read()

with open("runCase.py",encoding='utf-8') as f:
    f.write()
logger.info(con)