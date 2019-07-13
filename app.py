#!/usr/bin/env python3

import os
import yaml
from aws_cdk import core
from cdk_cloudtrail.cdk_cloudtrail_stack import CdkCloudTrailStack


DEFAULT_SPEC_FILE = './cloudtrail-spec.sample.yaml'


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



app = core.App()
#print(app.node.__dir__())
spec_file = app.node.try_get_context('spec-file')
cloudtrail_spec = scan_spec_file(spec_file)
#print(spec_file)
#print(cloudtrail_spec)
#print(cloudtrail_spec['tags'])

my_cloudtrail = CdkCloudTrailStack(app, "cdk-cloudtrail", tags=cloudtrail_spec['tags'])
app.synth()

#for tag in cloudtrail_spec['tags']:
#    print(tag)
#    my_tag = core.Tag(tag['key'], tag['value'])
#    print(my_tag.key)
#    print(my_tag.value)
#    #my_cloudtrail.node.apply_aspect(core.Tag(tag['key'], tag['value']))
#    my_cloudtrail.tags(core.Tag(tag['key'], tag['value']))

