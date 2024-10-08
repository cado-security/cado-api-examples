# Copyright 2024 Cado Security Ltd. All rights reserved #
#########################################################
#                     EC2 Acquisition                   #
#########################################################
#  Examples for importing EC2 evidence to the platform  #
#########################################################

import requests


def import_random_ec2_instance(base_url, token, project_id, cloud_id, region):
    """Get all ec2 instances and import the first one as new evidence
    to the given project

    :param str base_url: URL of the Cado Response server
    :param str token: API Key
    :param int project_id: project id to import the evidence to
    :param str cloud_id: cloud id configured in the platform
    :param str region: AWS region
    """

    # Get all ec2 instances in the given cloud_id (account) and region
    get_ec2_url = f'{base_url}/import/aws/ec2?cloud_id={cloud_id}&region={region}'
    ec2_instances = requests.get(
        get_ec2_url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    ).json()

    # Acquire the first instance in the response from above:
    post_ec2_url = f'{base_url}/import/aws/ec2'
    body_params = {
        'instance_id': ec2_instances['data'][0]['instance_id'],
        'cloud_id': cloud_id,
        'region': region,
        'project_id': project_id
    }
    result = requests.post(
        post_ec2_url,
        json=body_params,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    ).json()

    return result


if __name__ == '__main__':
    import config
    import_random_ec2_instance(
        config.API_URL,
        config.API_KEY,
        config.TEST_PROJECT_ID,
        config.CLOUD_ID,
        config.REGION
    )