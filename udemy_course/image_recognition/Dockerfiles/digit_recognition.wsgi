#! usr/bin/python

import sys
sys.path.insert(0, '/var/www/digit_recognition')
sys.path.insert(0, '/opt/conda/lib/python3.6/site-packages')
sys.path.insert(0, '/opt/conda/bin/')

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python'

from digit_recognition import app as application