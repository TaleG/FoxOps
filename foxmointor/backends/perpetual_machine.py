#_*_coding:utf-8_*_

import sys,os
import django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrazyMonitor.settings")
from FoxOps import settings

django.setup()
from  foxmointor import models
from foxmointor.backends import data_processing



if __name__ == '__main__':
    reactor = data_processing.DataHandler(settings)
    reactor.loopping()






