#   Copyright 2020 Cado Security Ltd. All rights reserved   #
#############################################################
#                      Overall example                      #
#############################################################
# This is a overall example that use a combination of sub-
# examples from the other modules in this folder (/examples).
# Check the folder(^) for more examples on a specific topic.
#############################################################
#                          STAGES:                          #
#  1) Authenticate with the api
#  2) Create new project
#  3) Import test data
#  4) Retrieve the data with different filters 
#############################################################
import requests
from time import sleep
from random import randint
import config


#################################################
# 1. Authenticate:
print('Generate access token:')
auth_url = config.API_URL + '/auth'
body_params = {
    'username': config.USERNAME,
    'password': config.PASSWORD
}
print(f'->> POST - {auth_url}')
auth_result = requests.post(auth_url, json=body_params)
access_token = auth_result.json()['token']


#################################################
# 2. Create new project:
print('Create new project:')
projects_url = config.API_URL + '/projects'
print(f'->> POST - {projects_url}')
new_project_name = 'newProject' + str(randint(0, 10000))
body_params = {'caseName': new_project_name}
project_result = requests.post(
    projects_url,
    json=body_params,
    headers={
        'Authorization': 'Bearer ' + access_token
    }
)
project_id = project_result.json()['id']


#################################################
# 3. Upload test data:
print('Upload test data:')
upload_url = f'{config.API_URL}/projects/{project_id}/imports/upload'
print(f'->> POST - {upload_url}')
data = {
    'file': open('./data/import_test.dd', 'rb') # read file binary
}
upload_result = requests.post(
    upload_url,
    headers={
        'Authorization': 'Bearer ' + access_token
    },
    files=data
)

print('Sleeping 5 minutes until data will be process...')
sleep(300)
print('Wake up')


#################################################
# 4. Search the timeline:
print('Get first 10 results from the timeline:')
timeline_url = f'{config.API_URL}/projects/{project_id}/timeline?perpage=10'
print(f'->> GET - {upload_url}')
timeline_result = requests.get(
    timeline_url,
    headers={
        'Authorization': 'Bearer ' + access_token
    },
)

print('results:')
print(timeline_result.json())