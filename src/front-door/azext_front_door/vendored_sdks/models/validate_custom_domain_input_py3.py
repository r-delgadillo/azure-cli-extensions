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


class ValidateCustomDomainInput(Model):
    """Input of the custom domain to be validated for DNS mapping.

    All required parameters must be populated in order to send to Azure.

    :param host_name: Required. The host name of the custom domain. Must be a
     domain name.
    :type host_name: str
    """

    _validation = {
        'host_name': {'required': True},
    }

    _attribute_map = {
        'host_name': {'key': 'hostName', 'type': 'str'},
    }

    def __init__(self, *, host_name: str, **kwargs) -> None:
        super(ValidateCustomDomainInput, self).__init__(**kwargs)
        self.host_name = host_name
