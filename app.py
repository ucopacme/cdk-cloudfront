#!/usr/bin/env python3

import os
import yaml
from aws_cdk import cdk
from cdk_cloudtrail.cdk_cloudtrail_stack import CdkCloudTrailStack


DEFAULT_SPEC_FILE = './cloudtrail_spec.yaml'


def scan_spec_file(spec_file):
    if spec_file is None:
        spec_file = DEFAULT_SPEC_FILE
    spec_file = os.path.expanduser(spec_file)
    if not os.path.isfile(spec_file):
        #log.error("spec_file not found: {}".format(spec_file))
        print("spec_file not found: {}".format(spec_file))
        return None
    #log.debug("loading spec file: {}".format(spec_file))
    with open(spec_file) as f:
        try:
            spec = yaml.safe_load(f.read())
        except (yaml.scanner.ScannerError, UnicodeDecodeError):
            #log.error("{} not a valid yaml file".format(spec_file))
            print("{} not a valid yaml file".format(spec_file))
            return None
        except Exception as e:
            #log.error("cant load spec_file '{}': {}".format(spec_file, e))
            print("cant load spec_file '{}': {}".format(spec_file, e))
            return None
    #log.debug("spec: {}".format(config))
    return spec



app = cdk.App()
#print(app.node.__dir__())
spec_file = app.node.get_context('spec-file')
print(spec_file)
cloudtrail_spec = scan_spec_file(spec_file)
print(cloudtrail_spec)

my_cloudtrail = CdkCloudTrailStack(app, "cdk-cloudtrail", **cloudtrail_spec)
for tag in cloudtrail_spec['tags']:
    my_cloudtrail.node.apply(cdk.Tag(tag['key'], tag['value']))

app.run()
