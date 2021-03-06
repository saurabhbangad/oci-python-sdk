# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataGuardAssociationToExistingDbSystemDetails(CreateDataGuardAssociationDetails):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataGuardAssociationToExistingDbSystemDetails object with values from values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDataGuardAssociationToExistingDbSystemDetails.creation_type` attribute
        of this class is ``ExistingDbSystem`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param creation_type:
            The value to assign to the creation_type property of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :type creation_type: str

        :param database_admin_password:
            The value to assign to the database_admin_password property of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :type database_admin_password: str

        :param protection_mode:
            The value to assign to the protection_mode property of this CreateDataGuardAssociationToExistingDbSystemDetails.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"
        :type protection_mode: str

        :param transport_type:
            The value to assign to the transport_type property of this CreateDataGuardAssociationToExistingDbSystemDetails.
            Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC"
        :type transport_type: str

        :param peer_db_system_id:
            The value to assign to the peer_db_system_id property of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :type peer_db_system_id: str

        """
        self.swagger_types = {
            'creation_type': 'str',
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str',
            'peer_db_system_id': 'str'
        }

        self.attribute_map = {
            'creation_type': 'creationType',
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType',
            'peer_db_system_id': 'peerDbSystemId'
        }

        self._creation_type = None
        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None
        self._peer_db_system_id = None
        self._creation_type = 'ExistingDbSystem'

    @property
    def peer_db_system_id(self):
        """
        Gets the peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        The `OCID`__ of the DB System to create the standby database on.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :rtype: str
        """
        return self._peer_db_system_id

    @peer_db_system_id.setter
    def peer_db_system_id(self, peer_db_system_id):
        """
        Sets the peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        The `OCID`__ of the DB System to create the standby database on.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param peer_db_system_id: The peer_db_system_id of this CreateDataGuardAssociationToExistingDbSystemDetails.
        :type: str
        """
        self._peer_db_system_id = peer_db_system_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
