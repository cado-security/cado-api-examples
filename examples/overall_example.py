#   Copyright 2020 Cado Security Ltd. All rights reserved   #
#############################################################
#                      Overall example                      #
#############################################################
# This is a overall example that use a combination of
# sub-examples from other modules in the folder (/examples)
# Check that folder(^) for more examples on a specific topic.
#############################################################
#                          STAGES:                          #
#  1) Authenticate with the api
#  2) Create new project
#  3) Import test data
#  4) Retrieve the data with different filters 
#  5) Create notes on some of the events
#############################################################
import config
from .authentication import generate_fresh_access_token

if __name__ == '__main__':
    pass