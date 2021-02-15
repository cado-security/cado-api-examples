# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#   This module shows different ways to retrieve data   #
#          from the timeline api resource               #
#########################################################
#                       Notes:                          #
# This url of this resource is:                         #
# /projects/<int:project_id/timeline                    #
#######################################################

# We can query the timeline by the following arguments:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1) `from_timestamp`
# 2) `to_timestamp`
## -> Both are unix timestamp formats
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3) `severity` and `alarm_severity`
## ->
### `severity` is a range, so given 5 it will be 1-5 (there's up to 10 different severities)
### If you want a specific severity (not a range), you can use the arg `alarm_severity` instead
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 4) `evidence_id`
## -> Get events only from a specefic evidence
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5) `query`
## ->
### Search for query (str) across all fields, so for example, if query=127.0.0.1
### It will search 127.0.0.1 in all the timeline columns (short, filename, etc...)
### We can also query a speceifc field, instead of cross-fields like with the `query` arg.
### The supported arugements for specefic field-search are: 
### `tag`, `user`, `executed_process`, `source_hostname`
### (We can add more, it's just a white list of fields that are allowed to search by)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 6) `pivot`
## ->
### pivot is a unique time filtering, given a pivot argument (unix timestamp format)
### It will show results from the time of the given pivot +- 2 minutes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PAGINATION - we can paginate the results using the args:
# 7) page
# 8) perpage (default is 100 per page)

import requests
import config


def pagination(token):
    """
    """
    result = requests.get(
        f'{BASE_URL}?page=2&perpage=500'
    ).json()
    result['page'] # What page are we?
    result['per_page'] # How much shown in this page
    result['pages'] # how many pages there's
    result['total'] # All total result for that specefic searchj
    result['results'] # Timeline results


#################
# Results for a specefic evidence id:
result = requests.get(
    f'{BASE_URL}?evidence_id=1'
).json()
result['results'] # Timeline results


#################
# severity RANGE:
result = requests.get(
    f'{BASE_URL}?severity=5'
).json()
result['results'] # Will show results with severity from 1-5


# ################# NOTE: There's small problem with that example, it's a quick fix, I'll do it this week
# # SPECIFIC severity:
# result = requests.get(
#     f'{BASE_URL}?alarm_severity=3'
# ).json()
# print(result)
# result['results'] # Will show only results with severity 3


#################
# TIME range severity:
result = requests.get(
    f'{BASE_URL}?from_timestamp=0&to_timestamp=5000'
).json()
result['results'] # Probs won't shows results as we don't have things between 0-5000 timestamp, but this is the concept


#################
# TIME range severity 2:
# We can also use only one of the timeranges (from_timestamp or to_timestamp)
result = requests.get(
    f'{BASE_URL}?from_timestamp=0'
).json()
result['results'] # Should return results as if we won't send any time range because we start from the very beggening (0)


#################
# Specefic fiels search
result = requests.get(
    f'{BASE_URL}?tag=File'
).json()
result['results'] # Results with tags that contains the word `File`, prob `File Access`..




