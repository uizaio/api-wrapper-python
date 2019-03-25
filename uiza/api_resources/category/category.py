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
        self.category_relation_url = set_url(
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
        :return: tuple of response data and status code
        """
        self.connection.url = self.category_relation_url
        data_body = dict(
            entityId=entity_id,
            metadataIds=metadata_ids
        )
        result = self.connection.post(data_body)

        return result

    def delete_relation(self, entity_id, metadata_ids):
        """
        Delete relation for entity and category
        :param entity_id: identifier of entity
        :param metadata_ids: identifier of category
        :return: tuple of response data and status code
        """
        self.connection.url = self.category_relation_url
        data_body = dict(
            entityId=entity_id,
            metadataIds=metadata_ids
        )
        result = self.connection.delete(data_body)

        return result
