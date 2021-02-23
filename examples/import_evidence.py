# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#  Examples for importing new evidence to the platform  #
#########################################################
#                      Base URL:                        #
#         /projects/<int:project_id>/imports           #
#########################################################
#                  QUICK EXPLANATION:                   #
# We can import evidence in several different ways:
#  1) Import AWS' EC2 instance
#  2) Import AWS' S3 bucket
#  3) Upload local evidence using request
#  4) Using EFS shared folder
# 
# 
#########################################################
import requests


def import_ec2_instance(base_url, token, project_id, instance, bucket):
    """Start a new task to acquire (import) the given instance id

    :param str base_url: api ip
    :param str token: access token
    :param int project_id: project primary key
    :param str instance: the instace_id to import (see get_instances example in this module)
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
        }
    )
    # work with the result:
    # result['task_id']
    return result


def import_random_ec2_instance(base_url, token, project_id):
    """Get all ec2 instances and import the first one as a new evidence
    to the given porject

    :param str base_url: api ip
    :param str token: access token
    :param int project_id: project primary key
    """
    url = f'{base_url}/projects/{project_id}/imports/ec2'
    # First, get all ec2 instaces:
    print(f'GET - {url}')
    ec2_instances = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        }
    ).json()

    # Then, get all s3 buckets (we need one to import ec2):
    print(f'GET - s3 buckets')
    s3_buckets = requests.get(
        url.replace('ec2', 's3'), # use s3 resource, not ec2
        headers={
            'Authorization': 'Bearer ' + token
        }
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
        }
    )
    # work with the result:
    # result['task_id']
    return result
    

def get_instances(base_url, token, project_id):
    """Get all ec2 instances

    :param str base_url: api ip
    :param str token: access token
    :param project_id: int, project primary key
    """
    url = f'{base_url}/projects/{project_id}/imports/ec2'
    print(f'GET - {url}')
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        }
    )
    
    # Working with the result
    # result.status_code
    # result = result.json()
    # result.json()['instances']
    return result


def upload_test_evidence(base_url, token, project_id):
    """Upload an evidence file and start a new task to process it
     -> This example show how to upload evidence using http request

    :param str base_url: api ip
    :param str token: access token
    :param project_id: int, project primary key
    """
    url = f'{base_url}/projects/{project_id}/imports/upload'
    print(f'POST - {url}')

    data = {
        'file': open('./data/import_test.dd', 'rb') # read file binary
    }
    result = requests.post(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        files=data
    )

    # work with the result:
    # result['task_id']
    return result


if __name__ == '__main__':
    import config
    from authentication import generate_fresh_access_token

    tokens = generate_fresh_access_token(
        config.API_URL,
        config.USERNAME,
        config.PASSWORD
    ).json()
    access_token = tokens['token']

    # upload_test_evidence(config.API_URL, access_token, config.TEST_PROJECT_ID)
    # import_random_ec2_instance(config.API_URL, access_token, config.TEST_PROJECT_ID)