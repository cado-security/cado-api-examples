# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#  Examples for importing new evidence to the platform  #
#########################################################
#                      Base URL:                        #
#         /projects/<int:project_id>/imports           #
#########################################################
#                  QUICK EXPLANATION:                   #
# We can import evidence in several different ways:
#  1) Import AWS EC2 instance
#  2) Import AWS S3 bucket
#  3) Upload local evidence using requests
# 
# 
#########################################################
import requests


def import_ec2_instance(base_url, token, project_id, instance, bucket):
    """Start a new task to acquire (import) the given instance id

    :param str base_url: URL of the Cado Response server
    :param str token: API Key
    :param int project_id: Project primary key
    :param str instance: The instance_id to import (see get_instances example in this module)
    :param str bucket:
    """
    url = f'{base_url}/projects/{project_id}/imports/ec2'
    print(f'POST - {url}')
    body_params = {
        'instance_id': instance,
        'bucket': bucket
    }
    result = requests.post(
        url,
        json=body_params,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    
    return result


def import_random_ec2_instance(base_url, token, project_id):
    """Get all ec2 instances and import the first one as a new evidence
    to the given project

    :param str base_url: URL of the Cado Response server
    :param str token: API Key
    :param int project_id: project primary key
    """
    url = f'{base_url}/projects/{project_id}/imports/ec2'
    # First, get all ec2 instaces:
    print(f'GET - {url}')
    ec2_instances = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    ).json()

    # Then, get all s3 buckets (we need one to import ec2):
    print(f'GET - s3 buckets')
    s3_buckets = requests.get(
        url.replace('ec2', 's3'), # use s3 resource, not ec2
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    ).json()

    # Acquire(import) the first one:
    print(f'POST - {url}')
    body_params = {
        'instance_id': ec2_instances['instances'][0]['id'],
        'bucket': s3_buckets['buckets'][0]
    }
    result = requests.post(
        url,
        json=body_params,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with the result:
    # result['task_id']
    return result
    

def get_instances(base_url, token, project_id):
    """Get all ec2 instances

    :param str base_url: URL of the Cado Response server
    :param str token: API Key
    :param int project_id: project primary key
    """
    url = f'{base_url}/projects/{project_id}/imports/ec2'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    
    # Working with the result
    # result.status_code
    # result = result.json()
    # result.json()['instances']
    return result


if __name__ == '__main__':
    import config
    import_random_ec2_instance(
        config.API_URL,
        config.API_KEY,
        config.TEST_PROJECT_ID
    )