#   Copyright 2024 Cado Security Ltd. All rights reserved   #
#############################################################
#                         Cado Host                         #
#############################################################
# How to generate cado host scripts using Cado Response API #
#############################################################
import logging
import subprocess
import requests

import config


# Cado Host Endpoint is: import/cado-host and it has the following query parameters:
# 1) os: windows, osx, osx-x86, linux, kubernetes
# 2) deployment: auto, manual  (download the cado host binary to the host machine or it is there already? usually use the `auto` option)
# 3) project_id


cado_host = requests.post(
    f'{config.API_URL}/import/cado-host',
    json={
        "os":"linux",
        "deployment":"auto",
        "project_id":config.TEST_PROJECT_ID,
        "command_options":{},
        "downloadable":False,
    },
    headers={'Authorization': f'Bearer {config.API_KEY}'},
    verify=False
).json()

command = f'set -e; set -x; {cado_host["data"]["command"]}'
logging.info(f'Running host script: {command}')
try:
    script_output = subprocess.check_output(['/bin/bash', '-c', command], stderr=subprocess.STDOUT).decode('utf-8')
    logging.info(f'Successful host command: {script_output}')
except subprocess.CalledProcessError as e:
    logging.exception(f'Failed command with message {e.output}')
    raise e
