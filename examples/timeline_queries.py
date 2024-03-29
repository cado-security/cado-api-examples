# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#       Examples for retrieving data from the timeline  #
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
### `severity` is a range, with 1 being malicious events
### 3 being suspicious or malicious evnets and 10 being
### all events
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

    -> for the purpose of the example, we provide defaults to the function parameters
       the defaults here is to get the second page of the timeline when there are 500 events per page

    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param int page: 
    :param int perpage:  
    """
    url = f'{base_url}/projects/{project_id}/timeline?page={page}&perpage={perpage}'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['page'] # What page are we?
    # result['per_page'] # How much is shown in this page
    # result['pages'] # How many pages are there
    # result['total'] # All total result for that specific search
    # result['results'] # Timeline results
    return result


def only_evidence_id(base_url, token, project_id, evidence_id=1):
    """Get timeline events for a specific evidence

    -> for the purpose of the example, we provide defaults to the function parameters

    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param int evidence_id: 
    """
    url = f'{base_url}/projects/{project_id}/timeline?evidence_id={evidence_id}'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['results'] # Timeline results
    return result


def severity_range(base_url, token, project_id, severity=5):
    """Get timeline events that are in a severity range
    
    -> for the purpose of the example, we provide defaults to the function parameters
       The default here is to filter by severity between 1-5

    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param int severity: top range for the severity attribute
    """
    url = f'{base_url}/projects/{project_id}/timeline?severity=5'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['results'] # results with severity from 1-5
    return result


def time_range(base_url, token, project_id, from_t=1581850873, to_t=1613473273):
    """Get timeline events that between time range
    time range defined by unix timestamp https://www.unixtimestamp.com/

    -> for the purpose of the example, we provide defaults to the function parameters

    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param int from_t: unix timestamp lower range
    :param int from_t: unix timestamp, the beginning of the range
    :param int to_t: unix timestamp, the end of the range
    """
    url = f'{base_url}/projects/{project_id}/timeline?from_timestamp={from_t}&to_timestamp={to_t}'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['results'] # results from 16.2.2020 to 16.2.2021
    return result


def pivot_results(
    base_url,
    token,
    project_id,
    pivot=1581850873
    ):
    """Get timeline events that occured 2 minutes before and after the given pivot timestamp

    -> for the purpose of the example, we provide defaults to the function parameters

    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param int pivot: unix timestamp
    """
    url = f'{base_url}/projects/{project_id}/timeline?pivot={pivot}'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    return result


def point_in_time(base_url, token, project_id):
    """Get timeline events from a specific point in time
    this examples shows that we can use from_timestamp OR to_timestamp as individuals

    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    """
    url = f'{base_url}/projects/{project_id}/timeline?from_timestamp=0'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
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

    -> for the purpose of the example, we provide defaults to the function parameters
        the default here is to search `File` events by looking in the `tag` column

    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param str field: the field to search in
    :param str value: the value to search in the field^
    """
    url = f'{base_url}/projects/{project_id}/timeline?{field}={value}'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    return result


def value_across_fields(
    base_url,
    token,
    project_id,
    query='127.0.0.1'
    ):
    """Get timeline events that have the given value in one of the fields

    -> for the purpose of the example, we provide defaults to the function parameters
        the default here is to search the IP `127.0.0.1` in the events

    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param str query: 
    """
    url = f'{base_url}/projects/{project_id}/timeline?query={query}'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    return result


if __name__ == '__main__':
    # This example assume that there's an existing project
    # in the platform and some test data to work with
    import config

    print('***************<[--PAGINATION RESULTS--]>***************')
    result = pagination(
        base_url=config.API_URL,
        token=config.API_KEY,
        project_id=config.TEST_PROJECT_ID
    )
    if result.status_code == 200:
        print(result.json())
    else:
        print('Cannot get timeline result: ', result.status_code)