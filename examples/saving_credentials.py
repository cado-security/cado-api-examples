"""
Copyright 2023 Cado Security Ltd. All rights reserved

This is an example of adding roles to the platform over the API.
To use, set the Platform API and Secret Key in config.py
Then add the roles to roles.csv in the format:
role,alias
Where role is the full arn of the role, e.g. arn:aws:iam::0001:role/CadoResponseRole
And the Alias is the name you want to save the credentials under to be viewable in the UI, e.g. My Role
"""


import requests
import csv

import config

def post_role(base_url, token, role, alias):
    """Saves an AWS role to the platform
    
    :param str base_url: URL of Cado Response
    :param str token: API Key
    :param str role: The role to save
    :param str alias: The alias to save the credentials under
    """

    url = f'{base_url}/clouds'
    body_params = {
        "provider": "aws",
        "credentials": {
            "role": role
            },
        "cloud_id": alias
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

def post_role_batch(base_url, token, csv_file_path):
    """Saves a batch of AWS roles to the platform
    
    :param str base_url: URL of Cado Response
    :param str token: API Key
    :param str csv_file_path: Path to a CSV file containing the roles to save

    The CSV file should contain a single column with the roles to save.
    The roles will be saved in the platform with the alias being the last part of the role.
    """

    with open(csv_file_path, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            role = row[0]
            alias = row[1]
            response = post_role(
                base_url=base_url, 
                token=token,
                role=role,
                alias=alias,
            )
            print(f"Add Role: [{role} with Alias [{alias}], Status: {response.status_code}, Response: {response.text}")


if __name__ == '__main__':
    import config
    post_role_batch(
        config.API_URL,
        config.API_KEY,
        "roles.csv"
    )