#/usr/bin/python2.7

import boto.ec2
import sys
import time
import datetime
import ConfigParser

def main():
    try:
        global region
        global accessKeyId
        global accessKeySecret

        now = datetime.datetime.now()
        print now.strftime('Running schedule at %d/%m/%Y %H:%M:%S')

        if len(sys.argv) < 3:
            print('The Action and Instance must be defined {start|stop|status} {instanceName}')
            sys.exit()

        action  = sys.argv[1]
        ec2Name = sys.argv[2]

        config = ConfigParser.ConfigParser()
        config.read("config.ini")

        accessKeyId     = config.get('credentials', 'aws_access_key_id')
        accessKeySecret = config.get('credentials', 'aws_secret_access_key')
        region          = config.get('config', 'region')
        ec2Id           = config.get('instances', ec2Name)

        if action == "start":
            startInstance(ec2Id)
        elif action == "stop":
            stopInstance(ec2Id)
        elif action == "status":
            printStatusInstance(ec2Id)
        else:
            print "Wrong action defined {start|stop}\n"
    except Exception, e:
        error = "Error: %s" % str(e)
        print(error)
        sys.exit(0)

def startInstance(ec2Id):
    print "Starting instance..."
    ec2 = boto.ec2.connect_to_region(region, aws_access_key_id=accessKeyId, aws_secret_access_key=accessKeySecret)
    ec2.start_instances(instance_ids=ec2Id)
    print('Instance Id : ' + ec2Id)
    print('Command processed...')
    time.sleep(5)
    print('Instance Status : ' + statusInstance(ec2Id))

def stopInstance(ec2Id):
    print "Stopping instance..."
    ec2 = boto.ec2.connect_to_region(region, aws_access_key_id=accessKeyId, aws_secret_access_key=accessKeySecret)
    ec2.stop_instances(instance_ids=ec2Id)
    print('Instance Id : ' + ec2Id)
    print('Command processed...')
    time.sleep(10)
    print('Instance Status : ' + statusInstance(ec2Id))

def statusInstance(ec2Id):
    ec2 = boto.ec2.connect_to_region(region, aws_access_key_id=accessKeyId, aws_secret_access_key=accessKeySecret)
    monitor = ec2.get_only_instances(instance_ids=ec2Id)
    return(monitor[0].state)

def printStatusInstance(ec2Id):
    print "Checking instance status:"
    ec2 = boto.ec2.connect_to_region(region, aws_access_key_id=accessKeyId, aws_secret_access_key=accessKeySecret)
    monitor = ec2.get_only_instances(instance_ids=ec2Id)
    for instance in monitor:
        print instance.id + ' : ' + instance.state
    sys.exit(0)


if __name__ == '__main__':
    main()