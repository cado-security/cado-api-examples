# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#   This module shows different ways to retrieve data   #
#          from the timeline api resource               #
#########################################################
#                       Notes:                          #
# This url of this resource is:                         #
# /projects/<int:project_id/timeline                    #
#######################################################

# We can query the timeline by the following arguments:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1) `from_timestamp`
# 2) `to_timestamp`
## -> Both are unix timestamp formats
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3) `severity` and `alarm_severity`
## ->
### `severity` is a range, so given 5 it will be 1-5 (there's up to 10 different severities)
### If you want a specific severity (not a range), you can use the arg `alarm_severity` instead
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 4) `evidence_id`
## -> Get events only from a specific evidence
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5) `query`
## ->
### Search for query (str) across all fields, so for example, if query=127.0.0.1
### It will search 127.0.0.1 in all the timeline columns (short, filename, etc...)
### We can also query a speceifc field, instead of cross-fields like with the `query` arg.
### The supported arugements for specific field-search are: 
### `tag`, `user`, `executed_process`, `source_hostname`
### (We can add more, it's just a white list of fields that are allowed to search by)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 6) `pivot`
## ->
### pivot is a unique time filtering, given a pivot argument (unix timestamp format)
### It will show results from the time of the given pivot +- 2 minutes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PAGINATION - we can paginate the results using the args:
# 7) page
# 8) perpage (default is 100 per page)
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
    result = requests.get(f'{BASE_URL}?page={page}&perpage={perpage}')
    result = result.json()
    # result['page'] # What page are we?
    # result['per_page'] # How much shown in this page
    # result['pages'] # how many pages there's
    # result['total'] # All total result for that specific searchj
    # result['results'] # Timeline results
    return result


def filter_by_evidence_id(base_url, token, project_id, evidence_id=1):
    """Get timeline events for a specific evidence

    -> for the purpose of the example, we provided defaults to the function parameters

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    :param evidence_id: int,
    """
    result = requests.get(f'{BASE_URL}?evidence_id={e_evidence_idid}')
    result = result.json()
    # result['results'] # Timeline results
    return result


def filter_by_severity_range(base_url, token, project_id, severity=5):
    """Get timeline events that are in a severity range
    
    -> for the purpose of the example, we provided defaults to the function parameters
       The default here is to filter by severity between 1-5

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    :param severity: int, top range for the severity attribute
    """
    result = requests.get(f'{BASE_URL}?severity=5')
    result = result.json()
    # result['results'] # results with severity from 1-5
    return result


def filter_by_time_range(base_url, token, project_id, from_t=1581850873, to_t=1613473273):
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
    result = requests.get(f'{BASE_URL}?from_timestamp=1581850873&to_timestamp=1613473273')
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
    result = requests.get(f'{BASE_URL}?pivot={pivot}')
    result = result.json()
    return result


def filter_by_point_in_time(base_url, token, project_id):
    """Get timeline events from a a specific point in time
    this examples shows that we can use from_timestamp OR to_timestamp as individuals

    :param base_url: str, api ip
    :param token: str, access token
    :param project_id: int, project primary key
    """
    result = requests.get(f'{BASE_URL}?from_timestamp=0')
    result = result.json()
    # result['results'] # Should return results as if we won't send any time range because we start from the very beggening (0)
    return result


def filter_by_specific_field_value(
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
    result = requests.get(f'{BASE_URL}?{field}={value}')
    result = result.json()
    return result


def filter_by_value_across_fields(
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
    result = requests.get(f'{BASE_URL}?query={query}')
    result = result.json()
    return result


if __name__ == '__main__':
    import config
