# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#       Examples for retrieving data from timeline      #
#########################################################
#                      Base URL:                        #
#         /projects/<int:project_id>/timeline           #
#########################################################
#                  QUICK EXPLANATION:                   #
# We can query the timeline by the following arguments: #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1) `from_timestamp`
# 2) `to_timestamp`
## -> Both are unix timestamp formats
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3) `severity` and `alarm_severity`
## ->
### `severity` is a range, so by given 5
### the range will be between 1-5 (up to 10 severities)
### If you want a specific severity (not a range),
### you can use the arg `alarm_severity` instead
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 4) `evidence_id`
## -> Get events only from a specific evidence
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5) `query`
## ->
### Search for query (string) across all fields,
### so for example, if query=127.0.0.1 It will search it
### in all the timeline columns (short, filename, etc...).
### Instead, We can also search in a specific field
### The supported arugements for specific field-search are: 
### `tag`, `user`, `executed_process`, `source_hostname`
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 6) `pivot`
## ->
### pivot is a unique time filtering,
### given a pivot argument (unix timestamp format)
### it will return results that occured in the range of
### two minutes before and after the given pivot
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PAGINATION - we can paginate the results using the args:
# 7) page
# 8) perpage (default is 100 per page)

#########################################################

import requests


def pagination(base_url, token, project_id, page=2, perpage=500):
    """Get timeline events and modify the default pagination parameters

    -> for the purpose of the example, we provided defaults to the function parameters
       the defaults here is to get the second page of the timeline when there's 500 events per page

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    :param page: int, 
    param perpage:
    """
    url = f'{base_url}?page={page}&perpage={perpage}'
    print(f'GET - {url}')
    result = requests.get(url)
    result = result.json()
    # result['page'] # What page are we?
    # result['per_page'] # How much shown in this page
    # result['pages'] # how many pages there's
    # result['total'] # All total result for that specific searchj
    # result['results'] # Timeline results
    return result


def only_evidence_id(base_url, token, project_id, evidence_id=1):
    """Get timeline events for a specific evidence

    -> for the purpose of the example, we provided defaults to the function parameters

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    :param evidence_id: int,
    """
    url = f'{base_url}?evidence_id={evidence_id}'
    print(f'GET - {url}')
    result = requests.get(url)
    result = result.json()
    # result['results'] # Timeline results
    return result


def severity_range(base_url, token, project_id, severity=5):
    """Get timeline events that are in a severity range
    
    -> for the purpose of the example, we provided defaults to the function parameters
       The default here is to filter by severity between 1-5

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    :param severity: int, top range for the severity attribute
    """
    url = f'{base_url}?severity=5'
    print(f'GET - {url}')
    result = requests.get(url)
    result = result.json()
    # result['results'] # results with severity from 1-5
    return result


def time_range(base_url, token, project_id, from_t=1581850873, to_t=1613473273):
    """Get timeline events that between time range
    time range defined by unix timestamp https://www.unixtimestamp.com/

    -> for the purpose of the example, we provided defaults to the function parameters

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    :param from_t: int, unix timestamp lower range
    :param from_t: int, unix timestamp, the beginning of the range
    :param to_t: int, unix timestamp, the end of the range
    """
    url = f'{base_url}?from_timestamp={from_t}&to_timestamp={to_t}'
    print(f'GET - {url}')
    result = requests.get(url)
    result = result.json()
    # result['results'] # results from 16.2.2020 to 16.2.2021
    return result


def pivot_results(
    base_url,
    token,
    project_id,
    pivot=1581850873
    ):
    """Get timeline events that occured 2 minutes beforer and after the given pivot timestamp

    -> for the purpose of the example, we provided defaults to the function parameters

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    :param pivot: int, unix timestamp
    """
    url = f'{base_url}?pivot={pivot}'
    print(f'GET - {url}')
    result = requests.get(url)
    result = result.json()
    return result


def point_in_time(base_url, token, project_id):
    """Get timeline events from a a specific point in time
    this examples shows that we can use from_timestamp OR to_timestamp as individuals

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    """
    url = f'{base_url}?from_timestamp=0'
    print(f'GET - {url}')
    result = requests.get(url)
    result = result.json()
    # result['results'] # Should return results as if we won't send any time range because we start from the very beggening (0)
    return result


def specific_field_value(
    base_url,
    token,
    project_id,
    field='tag',
    value='file'
    ):
    """Get timeline events filter by specific field value,

    -> for the purpose of the example, we provided defaults to the function parameters
        the default here is to search `File` events by looking in the `tag` column

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    :param field: str, the field to search in
    :param value: str, the value to search in the field^
    """
    url = f'{base_url}?{field}={value}'
    print(f'GET - {url}')
    result = requests.get(url)
    result = result.json()
    return result


def value_across_fields(
    base_url,
    token,
    project_id,
    query='127.0.0.1'
    ):
    """Get timeline events that has the gevin value in one of the fields,

    -> for the purpose of the example, we provided defaults to the function parameters
        the default here is to search the ip `127.0.0.1` in the events

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    :param query: str, 
    """
    url = f'{base_url}?query={query}'
    print(f'GET - {url}')
    result = requests.get(url)
    result = result.json()
    return result


if __name__ == '__main__':
    import config 
    from authentication import generate_fresh_access_token

    tokens = generate_fresh_access_token(
        config.BASE_URL,
        config.USERNAME,
        config.PASSWORD
    )
    access_token = tokens['token']

    print('***************<[--PAFINATION RESULTS--]>***************')
    result = pagination(base_url=config.BASE_URL, token=access_token)
    print(result)