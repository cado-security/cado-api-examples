# Cado API Code Examples
This repository contains code examples for integration with the Cado API using Python and the Requests library.

The examples assumes that you have the Cado Response platform and a user with admin privileges.

# Getting started
Before you can run any of the examples under the `./examples` folder you should follow these steps:

1. Prepare your platform:

Make sure your Cado Response platform is up and running and that you have an existing project with evidence imported (required for some of the examples, e.g. the timeline search example).

2. Create API Key
In the platform, go to Settings -> API -> Create New Key

Make a note of the Secret Key.

3. Clone the repository:
```
git clone https://github.com/cado-security/cado-api-examples.git
```

4. Make sure you have python3 installed

5. Edit `the examples/config.py` file to fit to your platform:
```python
PLATFORM_IP = '127.0.0.1'                   # Change to the IP of the platform
API_URL = f'https://{PLATFORM_IP}/api/v3'   # Don't edit this value
API_KEY = ''                                # API Key generated in settings
TEST_PROJECT_ID = 1                         # any project that already exists
CLOUD_ID = 'Default'                        # A cloud id that's already configured in the platform
REGION = 'us-east-1'                        # A region in AWS that has available EC2 instances
```

7. Run examples!
An End-to-End example can be found in the module [end_to_end_example.py](examples/end_to_end_example.py)!
to run the example:
```
python3 examples/end_to_end_example.py
```

8. Note:

There are many examples and explanations inside each module.

Only a few of the examples run automatically when executing the module as in the above^ so please open and read each module for full explanation and examples on a specific topic.

```
python3 examples/timeline_queries.py
```
