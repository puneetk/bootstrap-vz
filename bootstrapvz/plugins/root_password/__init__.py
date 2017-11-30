# -*- coding: utf-8 -*-
"""
bootstrapvz.plugins.root_password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


"""

#pylint: disable=unused-argument
def validate_manifest(data, validator, error):
    """ validate_manifest """
    from bootstrapvz.common.tools import rel_path
    validator(data, rel_path(__file__, 'manifest-schema.yml'))

def resolve_tasks(taskset, manifest):
    """ resolve_tasks """
    from bootstrapvz.common.tasks import ssh
    from bootstrapvz.plugins.root_password.tasks import SetRootPassword
    taskset.discard(ssh.DisableSSHPasswordAuthentication)
    taskset.add(ssh.EnableRootLogin)
    taskset.add(SetRootPassword)
