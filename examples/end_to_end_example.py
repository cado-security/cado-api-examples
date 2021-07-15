#   Copyright 2020 Cado Security Ltd. All rights reserved   #
#############################################################
#                      Overall example                      #
#############################################################
# This is a overall example that use a combination of sub-
# examples from the other modules in this folder (/examples).
# Check the folder(^) for more examples on a specific topic.
#############################################################
#                          STAGES:                          #
#  1) Create new project
#  2) Import test data
#  3) Retrieve the data with different filters 
#############################################################
import requests
import urllib3
from time import sleep
from random import randint

import config

print('**************************************')
print('About to preform the following stages:')
print('1) Create new project')
print('2) Get random ec2 instance id to import')
print('3) Import ec2 instance base on id^')
print('4) Retrieve the data with different filters ')
print('**************************************')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#################################################
# 1. Create new project:
print('Creating new project...')
projects_url = config.API_URL + '/projects'
print(f'->> POST - {projects_url}')
new_project_name = 'newProject' + str(randint(0, 10000))
body_params = {'caseName': new_project_name}
project_result = requests.post(
    projects_url,
    json=body_params,
    headers={
        'Authorization': 'Bearer ' + config.API_KEY
    },
    verify=False
)
project_id = project_result.json()['id']


#################################################
# 2. Get random ec2 instance id to import:
print('Getting ec2 instance from the cloud...')
get_ec2_instances_url = f'{config.API_URL}/projects/{project_id}/imports/ec2'
print(f'->> GET - {get_ec2_instances_url}')
instances_results = requests.get(
    get_ec2_instances_url,
    headers={'Authorization': 'Bearer ' + config.API_KEY},
    verify=False
)
first_instance = instances_results.json()['instances'][0]['id']

#################################################
# 3. Import instance
print('About to import instance: ', first_instance)
body_params = {'instance_id': first_instance, 'bucket': ''}
result = requests.post(
    get_ec2_instances_url,
    json=body_params,
    headers={
        'Authorization': 'Bearer ' + config.API_KEY
    },
    verify=False
)

print('Sleeping 5 minutes until data will be process...')
sleep(300)
print('Wake up')

#################################################
# 4. Search the timeline:
print('Get first 10 results from the timeline:')
timeline_url = f'{config.API_URL}/projects/{project_id}/timeline?perpage=10'
print(f'->> GET - {timeline_url}')
timeline_result = requests.get(
    timeline_url,
    headers={
        'Authorization': 'Bearer ' + config.API_KEY
    },
    verify=False
)

print('results:')
print(timeline_result.json())