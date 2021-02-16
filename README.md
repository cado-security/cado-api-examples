# Cado API code examples
This repository contains code examples for integrate with Cado API using python and the requests library.
The examples assumes that you have Cado Response platform up and running and that you have a user with admin privileges.

# Getting started
Before you can run any of the examples under the `./examples` folder you first need to
do the following steps:
1. Clone the repository:
```
git clone https://github.com/cado-security/cado-api-examples.git
```
2. Prepare your platform:
Make sure your Cado Response platform is running and that you have an existing project and evidence imported (required for some of the examples, e.g. timeline searching examples)
3. Edit `the examples/config.py` file to fit to your platform:
```
PLATFORM_IP = '127.0.0.1'                   # Change to the ip of the platform
API_URL = f'http://{PLATFORM_IP}:5000'      # Don't edit this value
USERNAME = ''                               # Username for admin user
PASSWORD = ''                               # Password for the user^
TEST_PROJECT_ID = 1                         # project that already exists
``` 
