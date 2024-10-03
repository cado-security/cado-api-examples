#   Copyright 2024 Cado Security Ltd. All rights reserved   #
#############################################################
#         Manage projects in the platform examples          #
#############################################################
# This module includes examples for management project in the
# platform. For example:
#   1) Create new a new project
#   2) Delete existing project
#############################################################
import requests


def create_new_project(base_url, token, name):
    """Create a new project in the platform

    :param str base_url: URL of the Cado Response server
    :param str token: API Key
    :param str name: The name of the new project
    """
    url = f"{base_url}/projects"
    body_params = {"case_name": name}
    result = requests.post(url, json=body_params, headers={"Authorization": "Bearer " + token}, verify=False)

    return result


def delete_project(base_url, token, project_id):
    """delete given project

    :param str base_url:  URL of the Cado Response server
    :param str token: API Key
    :param int project_id: The ID of the project to delete
    """
    url = f"{base_url}/projects/{project_id}"
    result = requests.delete(url, headers={"Authorization": "Bearer " + token}, verify=False)

    return result


if __name__ == "__main__":
    from random import randint

    import config

    # Create a new project
    random_project_name = "project_" + str(randint(0, 10000))
    create_project_result = create_new_project(config.API_URL, config.API_KEY, random_project_name)
    project_id = create_project_result.json()["data"]["id"]
    if create_project_result.status_code == 201:
        print("New project created: ", random_project_name)
    else:
        quit("Cannot create project: " + str(create_project_result.status_code))
    delete_project_result = delete_project(config.API_URL, config.API_KEY, project_id)
    if delete_project_result.status_code == 200:
        print("Project deleted: ", project_id)
