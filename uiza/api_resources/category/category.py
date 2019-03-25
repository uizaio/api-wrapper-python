import uiza
from uiza import Connection
from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url


class Category(UizaBase):

    def __init__(self):
        self.connection = Connection(workspace_api_domain=uiza.workspace_api_domain, api_key=uiza.authorization)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.category.type,
            api_version=settings.uiza_api.category.version,
            api_sub_url=settings.uiza_api.category.sub_url
        )
        self.category_relation_entity_url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.category.type,
            api_version=settings.uiza_api.category.version,
            api_sub_url='media/metadata/related/entity'
        )
        self.category_relation_metadata_url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.category.type,
            api_version=settings.uiza_api.category.version,
            api_sub_url='media/entity/related/metadata'
        )

    def create_relation(self, entity_id, metadata_ids):
        """
        Create relation for entity and category
        :param entity_id: identifier of entity
        :param metadata_ids: identifier of category
        """
        self.connection.url = self.category_relation_metadata_url
        data_body = dict(
            entityId=entity_id,
            metadataIds=metadata_ids,
            appId=uiza.app_id
        )
        result = self.connection.post(data_body)

        return result

    def create_relation_entity(self, entity_ids, metadata_id):
        """
        Create relation for entity and category
        :param entity_ids: identifier of entity
        :param metadata_id: identifier of category
        """
        self.connection.url = self.category_relation_entity_url
        data_body = dict(
            entityIds=entity_ids,
            metadataId=metadata_id,
            appId=uiza.app_id
        )
        result = self.connection.post(data_body)

        return result

    def delete_relation(self, entity_id, metadata_ids):
        """
        Delete relation for entity and category
        :param entity_id: identifier of entity
        :param metadata_ids: identifier of category
        """
        self.connection.url = self.category_relation_metadata_url
        data_body = dict(
            entityId=entity_id,
            metadataIds=metadata_ids,
            appId=uiza.app_id
        )
        result = self.connection.delete(data_body)

        return result

    def delete_relation_entity(self, entity_ids, metadata_id):
        """
        Delete relation for entity and category
        :param entity_ids: identifier of entity
        :param metadata_id: identifier of category
        """
        self.connection.url = self.category_relation_entity_url
        data_body = dict(
            entityIds=entity_ids,
            metadataId=metadata_id,
            appId=uiza.app_id
        )
        result = self.connection.delete(data_body)

        return result
