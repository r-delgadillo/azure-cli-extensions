# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ManagedRuleGroupOverride(Model):
    """Defines a managed rule group override setting.

    All required parameters must be populated in order to send to Azure.

    :param rule_group_name: Required. Describes the managed rule group to
     override.
    :type rule_group_name: str
    :param rules: List of rules that will be disabled. If none specified, all
     rules in the group will be disabled.
    :type rules: list[~azure.mgmt.frontdoor.models.ManagedRuleOverride]
    """

    _validation = {
        'rule_group_name': {'required': True},
    }

    _attribute_map = {
        'rule_group_name': {'key': 'ruleGroupName', 'type': 'str'},
        'rules': {'key': 'rules', 'type': '[ManagedRuleOverride]'},
    }

    def __init__(self, **kwargs):
        super(ManagedRuleGroupOverride, self).__init__(**kwargs)
        self.rule_group_name = kwargs.get('rule_group_name', None)
        self.rules = kwargs.get('rules', None)
