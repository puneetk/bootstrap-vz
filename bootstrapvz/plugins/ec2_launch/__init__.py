# -*- coding: utf-8 -*-
"""
bootstrapvz.plugins.ec2_launch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


"""
#pylint: disable=unused-argument

import logging

from bootstrapvz.common.tools import rel_path
from bootstrapvz.plugins.ec2_launch import tasks

_LOGGER = logging.getLogger(__name__)

def validate_manifest(data, validator, error):
    """ validate_manifest """
    validator(data, rel_path(__file__, 'manifest-schema.yml'))


def resolve_tasks(taskset, manifest):
    """ resolve_tasks """
    taskset.add(tasks.LaunchEC2Instance)
    if 'print_public_ip' in manifest.plugins['ec2_launch']:
        taskset.add(tasks.PrintPublicIPAddress)
    if manifest.plugins['ec2_launch'].get('deregister_ami', False):
        taskset.add(tasks.DeregisterAMI)
