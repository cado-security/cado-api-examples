"""Copyright 2020 Cado Security Ltd. All rights reserved
"""
import requests

def generate_fresh_access_token(base_url, username, password):
    url = base_url + '/auth'
    
    