# cost_allocation_tags
AWS Lambda to print out all Active UserDefined Cost Allocation Tags

### Description
Per https://aws.amazon.com/about-aws/whats-new/2022/06/aws-cost-allocation-tag-api/ you can now
use an API to check which cost allocation tags are active so that you can pivot in your 
Cost and Usage Reports.
This Lambda prints out which UserDefined Cost Allocation Tags are Active

### Pre-requisites
* python 3.7 or higher
* setup the correct IAM permissions - this is done via the supplied YAML CFT
* this is a new AWS feature so you need boto3 >= 1.24 - in Lambda you can add this via a Layer

### Environment variables
* log_group_envvar : the name of the CW Log Group to output the log stream

### Example output
```
List the UserDefined cost allocation tags
TagKey,Type,Status
AC_ec2_billing_alarm,UserDefined,Active
```

### Triggers
This lambda can be run standalone or via a trigger eg daily via an EventBridge rule eg rate(1 day)
