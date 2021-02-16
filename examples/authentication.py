# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#  This module shows how to authenticate with Cado API  #
#########################################################
#                      Base URL:                        #
#                       /auth                           #
#########################################################
# There are several ways to authenticate with Cado API,
# most common and best practice is to use Access Tokens
# which can be generated using two different ways:
# 1) Using Username and Password
# 2) Using Refresh Token
# Initialy, you need to authenticate with the api
# using the first method (1^) which will generate "access
# token" and one additional token called "refresh token".
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

    # work with return value
    # result.status_code
    # result = result.json()
    # result['token'] # This is the access token
    # result['refresh_token']
    # result['user_id']
    return result


def generate_access_token_using_refresh_token(base_url, refresh_token):
    """Generate access token using refresh token
    -> this token is NOT FRESH

    :param base_url: str, api ip
    :param refresh_token: str,
    """
    url = base_url + '/auth/refresh'
    print(f'POST - {url}')
    result = requests.post(
        url,
        headers={
            'Authorization': 'Bearer ' + refresh_token
        }
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['access_token'] # This is the new, not fresh, access token
    return result


if __name__ == '__main__':
    import config 

    tokens = generate_fresh_access_token(
        config.API_URL,
        config.USERNAME,
        config.PASSWORD
    ).json()
    access_token = tokens['token']
    refresh_token = tokens['refresh_token']
    print('Fresh access token: ' + access_token)

    result = generate_access_token_using_refresh_token(
        base_url=config.API_URL,
        refresh_token=refresh_token
    ).json()
    print('Not fresh access token: ' + result['access_token'])