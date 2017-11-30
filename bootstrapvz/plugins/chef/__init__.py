# -*- coding: utf-8 -*-
"""
bootstrapvz.plugins.chef.tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


"""
#pylint: disable=unused-argument


from bootstrapvz.plugins.chef import tasks


def validate_manifest(data, validator, error):
    """ validate_manifest """
    from bootstrapvz.common.tools import rel_path
    validator(data, rel_path(__file__, 'manifest-schema.yml'))


def resolve_tasks(taskset, manifest):
    """ resolve_tasks """
    taskset.add(tasks.AddPackages)
    if 'assets' in manifest.plugins['chef']:
        taskset.add(tasks.CheckAssetsPath)
        taskset.add(tasks.CopyChefAssets)
