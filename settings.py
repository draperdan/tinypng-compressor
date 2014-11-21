"""
Settings
"""
from os import environ

API_KEY = environ.get('API_KEY', '{{ api_key }}')

ACCEPTED_EXTENSIONS = ['.png', '.jpg']
