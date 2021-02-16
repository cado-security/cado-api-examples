# Copyright 2020 Cado Security Ltd. All rights reserved #
#########################################################
#  Examples for importing new evidence to the platform  #
#########################################################
#                      Base URL:                        #
#         /projects/<int:project_id>/imports           #
#########################################################
#                  QUICK EXPLANATION:                   #
# We can import evidence in several different ways:
#  1) Import AWS' EC2 instance
#  2) Import AWS' S3 bucket
#  3) Upload local evidence using request
#  4) Using EFS shared folder
# It the examples here we'll focues on the first two.
#########################################################
import requests


if __name__ == '__main__':
    import config
    pass