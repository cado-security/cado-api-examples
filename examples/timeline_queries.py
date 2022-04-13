# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#       Examples for retrieving data from the timeline  #
#########################################################

import requests

def timeline_query(
    base_url,
    token,
    project_id,
    query='root'
    ):
    """ Simple example querying the Timeline

    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param str query: 
    """
    url = f'{base_url}/projects/{project_id}/logic?text={query}'
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
    result = timeline_query(
        base_url=config.API_URL,
        token=config.API_KEY,
        project_id=config.TEST_PROJECT_ID
    )
    if result.status_code == 200:
        print(result.json())
    else:
        print('Cannot get timeline result: ', result.status_code)