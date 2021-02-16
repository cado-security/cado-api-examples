"""Copyright 2020 Cado Security Ltd. All rights reserved
"""
import requests

def generate_fresh_access_token(base_url, username, password):
    """Access auth endpoint using username and password
    to generate Fresh Access Token

    :param base_url: str, 
    :param username: str, 
    :param password: str,  
    """
    url = base_url + '/auth'
    
    