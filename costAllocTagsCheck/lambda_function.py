# Lambda to print out all Active UserDefined Cost Allocation Tags
# Also logs results to CloudWatch log stream

import json
import boto3
import os
import botocore
from botocore.exceptions import ClientError
import uuid
import time
from datetime import datetime

ceClient = boto3.client('ce')
logsClient = boto3.client('logs')


def lambda_handler(event, context):

    
    # print(boto3.__version__)
    # print(botocore.__version__)
    
    # allow local Python execution testing
    execEnv = str(os.getenv('AWS_EXECUTION_ENV'))
    if execEnv.startswith("AWS_Lambda"):
        logGroupParam = os.getenv('log_group_envvar')
        log_group = str(logGroupParam)
    else:
        log_group = '/aws/lambda/costAllocTagsCheck'

    print("List the UserDefined cost allocation tags")
    print("TagKey,Type,Status")

    response = ceClient.list_cost_allocation_tags(
        Status='Active',
        Type='UserDefined'
    )

    tags = response['CostAllocationTags']
    for tg in tags:
        tgKey = tg['TagKey']
        tgStatus = tg['Status']
        tgType = tg['Type']
        print(tgKey, tgType, tgStatus, sep=",")

    return None


# allow local Python execution testing
if __name__ == '__main__':
    lambda_handler(None,None)
