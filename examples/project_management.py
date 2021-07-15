#   Copyright 2020 Cado Security Ltd. All rights reserved   #
#############################################################
#         Manage projects in the platform examples          #
#############################################################
# This module includes examples for management project in the
# platform. for example:
#   1) Create new and delete existing project
#   2) Update project's details
#   3) Enable access for users to a project
#############################################################
import requests


def create_new(base_url, token, name):
    """Create new project
    
    :param str base_url: api ip
    :param str token: API Key
    :param str name: name for the new project
    """
    url = f'{base_url}/projects'
    print(f'POST - {url}')
    body_params = {'caseName': name}
    result = requests.post(
        url,
        json=body_params,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['id'] # the id of the new project
    return result


def change_name(base_url, token, project_id, new_name):
    """Change project name
    
    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param str new_name: new name for the project
    """
    url = f'{base_url}/projects/{project_id}'
    print(f'PUT - {url}')
    body_params = {'caseName': new_name}
    result = requests.put(
        url,
        json=body_params,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['msg'] # SHould be 'Updated' and status code 200
    return result


def add_user_to_project(base_url, token, project_id, user):
    """Add user to have access to the given project
    
    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    :param str user: username to add
    """
    # First, get all current users of the project:
    url = f'{base_url}/projects/{project_id}'
    result = requests.get(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    current_users = result.json()['users']

    # Second, Add to the list the new user
    current_users.append(
        {'username': user}
    )

    # Then, send update request:
    body_params = {
        'users': current_users
    }
    result = requests.put(
        url,
        json=body_params,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['msg'] # SHould be 'Updated' and status code 200
    return result


def delete_project(base_url, token, project_id):
    """delete given project
    
    :param str base_url: api ip
    :param str token: API Key
    :param int project_id: project primary key
    """
    url = f'{base_url}/projects/{project_id}'
    print(f'DELETE - {url}')
    result = requests.delete(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['msg'] # SHould be 'Deleted' and status code 200
    return result


def delete_all_projects(base_url, token):
    """delete all projects in the platform
    
    :param str base_url: api ip
    :param str token: API Key
    """
    url = f'{base_url}/projects'
    print(f'DELETE - {url}')
    result = requests.delete(
        url,
        headers={
            'Authorization': 'Bearer ' + token
        },
        verify=False
    )
    # work with return value
    # result.status_code
    # result = result.json()
    # result['msg'] # Should be 'Deleted' and status code 200
    # result['count']
    return result



if __name__ == '__main__':
    from random import randint
    import config
    
    # Create new project
    random_project_name = 'project_' + str(randint(0, 10000))
    create_project_result = create_new(config.API_URL, config.API_KEY, random_project_name)
    if create_project_result.status_code == 201:
        print('New project created: ', random_project_name)
    else:
        quit('Cannot create project: ' + str(create_project_result.status_code))
    
    # Update the project's name
    project_id = create_project_result.json()['id']
    new_name = random_project_name + '_new'
    chnage_name_result = change_name(config.API_URL, config.API_KEY, project_id, new_name)
    if chnage_name_result.status_code == 200:
        print('Project name changed: ', new_name)
    else:
        quit('Cannot change project name: ' + str(chnage_name_result.status_code))
