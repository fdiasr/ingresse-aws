#Ingresse Cron - Schedule

This module is a tool to manage instances state on aws.

## Setup

Install boto to communicate with AWS:

    pip install boto

## Configuration

Rename config-example.ini, add your configuration as example :

    [credentials]
    aws_access_key_id = {your key id}
    aws_secret_access_key = {your access key}
    [config]
    region = us-east-1
    [instances]
    instance-name-1 = {instance_aws_id_1}
    instance-name-2 = {instance_aws_id_2}
    instance-name-3 = {instance_aws_id_3}

## Usage

Use this module, in the command line:

    python aws-schedule.py {action} {instance-name-1}

Actually action are : "*start*", "*stop*" and "*status*"

Important : We like use this tool into crontab.