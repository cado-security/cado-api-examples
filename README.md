# Cado API Code Examples
This repository contains code examples for integration with the Cado API using Python and the Requests library.
The examples assumes that you have the Cado Response platform and a user with admin privileges.

# Getting started
Before you can run any of the examples under the `./examples` folder you must follow these steps:

1. Read the Quick API Manual
[Click here](data/Cado_API_Quick_Start.pdf)

2. Prepare your platform:
Make sure your Cado Response platform is up and running and that you have an existing project with evidence imported (required for some of the examples, e.g. timeline searching examples).

3. Create API Key
In the platform, go to Settings -> API -> Create New Key
Keep the secret key

4. Clone the repository:
```
git clone https://github.com/cado-security/cado-api-examples.git
```

5. Make sure you have python3 installed

6. Edit `the examples/config.py` file to fit to your platform:
```python
PLATFORM_IP = '127.0.0.1'                   # Change to the ip of the platform
API_URL = f'http://{PLATFORM_IP}:5000'      # Don't edit this value
API_KEY = ''                                # API Key generated in settings
TEST_PROJECT_ID = 1                         # project that already exists
```

7. Run examples!
End-to-End example can be found in the module [end_to_end_example.py](examples/end_to_end_example.py)!
to run the examples:
```
python3 examples/end_to_end_example.py
```

8. Note:
There are many examples and explanations inside each module. Only few of the examples run automatically when executing the module as in the above^ so please open and read each module for full explantaion and examples on a specific topic.

```
python3 examples/timeline_queries.py
```
