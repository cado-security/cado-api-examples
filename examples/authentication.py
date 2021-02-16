# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#  This module shows how to authenticate with Cado API  #
#########################################################
#                      Base URL:                        #
#                       /auth                           #
#########################################################
# There are several ways to authenticate with Cado API,
# most common and best practice is to use Access Tokens
# which can be generated in using two different ways:
# 1) Using Username and Password
# 2) Using Refresh Token
# Initialy, you need to authenticate with the api
# using the first method (1^) which will generate
# access token and some other token called "refresh token".
# The access token will expire after 15 minutes and then
# you will need to re-generate it. you can do so using
# the same method as before (using username and passowrd)
# or you can use the refresh token instead.
# Where's the catch?
# An access token that was generated using refresh token
# can only be used for create/retrive/update operations
# while it cannot be used for delete operations.
# for that, you need a token that was generated using
# username & password - which also called "Fresh Token"
######################################################### 
import requests


def generate_fresh_access_token(base_url, username, password):
    """Access auth endpoint using username and password
    to generate Fresh Access Token and Refresh token

    :param base_url: str, api ip
    :param username: str, platform user
    :param password: str,  platform user's password
    """
    url = base_url + '/auth'
    body_params = {
        'username': username,
        'password': password
    }
    print(f'POST - {url}')
    result = requests.post(url, json=body_params)
    result = result.json()
    # result['token'] # This is the access token
    # result['refresh_token']
    # result['user_id']
    return result

