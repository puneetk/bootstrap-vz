# -*- coding: utf-8 -*-
"""
bootstrapvz.plugins.admin_user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


"""
#pylint: disable=unused-argument

import logging

from bootstrapvz.plugins.admin_user import tasks
from bootstrapvz.common.tools import rel_path
from bootstrapvz.common.tasks import ssh

_LOGGER = logging.getLogger(__name__)


def validate_manifest(data, validator, error):
    validator(data, rel_path(__file__, 'manifest-schema.yml'))


def resolve_tasks(taskset, manifest):

    from bootstrapvz.common.releases import jessie
    if manifest.release < jessie:
        taskset.update([ssh.DisableRootLogin])

    if 'password' in manifest.plugins['admin_user']:
        taskset.discard(ssh.DisableSSHPasswordAuthentication)
        taskset.add(tasks.AdminUserPassword)

    if 'pubkey' in manifest.plugins['admin_user']:
        taskset.add(tasks.CheckPublicKeyFile)
        taskset.add(tasks.AdminUserPublicKey)
    elif manifest.provider['name'] == 'ec2':
        _LOGGER.info("The SSH key will be obtained from EC2")
        taskset.add(tasks.AdminUserPublicKeyEC2)
    elif 'password' not in manifest.plugins['admin_user']:
        _LOGGER.warn("No SSH key and no password set")

    taskset.update([
        tasks.AddSudoPackage,
        tasks.CreateAdminUser,
        tasks.PasswordlessSudo,
    ])
