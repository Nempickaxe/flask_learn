#! usr/bin/python

import sys
sys.path.insert(0, '/var/www/flask_clustering_api')
sys.path.insert(0, '/opt/conda/lib/python3.6/site-packages')
sys.path.insert(0, '/opt/conda/bin/')

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python'

from flask_clustering_api import app as application