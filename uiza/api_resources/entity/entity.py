import uiza
from uiza import Connection
from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url


class Entity(UizaBase):

    def __init__(self):
        self.connection = Connection(workspace_api_domain=uiza.workspace_api_domain, api_key=uiza.authorization)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.entity.type,
            api_version=settings.uiza_api.entity.version,
            api_sub_url=settings.uiza_api.entity.sub_url
        )

    def search(self, keyword):
        """
        Search entity base on keyword entered
        :param keyword: keyword for search entity
        """
        self.connection.url = '{}/search'.format(self.connection.url)
        params = dict(keyword=keyword, appId=uiza.app_id)
        query = self.url_encode(params=params)
        data = self.connection.get(query=query)

        return data


    def generate_iframe(self, entityId, api):
        """
        Generate iframe entity base on keyword entered
        :param entityId: id of entity
        :param api: api iframe
        """
        self.connection.url = '{}/iframe'.format(self.connection.url)
        params = dict(entityId=entityId, api=api, appId=uiza.app_id)
        query = self.url_encode(params=params)
        data = self.connection.get(query=query)

        return data

    def publish(self, id):
        """
        Publish entity to CDN, use for streaming
        :param id: identifier of entity
        """
        self.connection.url = '{}/publish'.format(self.connection.url)
        data = self.connection.post(data={'id': id, 'appId': uiza.app_id})

        return data

    def get_status_publish(self, id):
        """
        Get status publish entity
        :param id: identifier of entity
        """
        self.connection.url = '{}/publish/status'.format(self.connection.url)
        query = self.url_encode(params={'id': id, 'appId': uiza.app_id})
        data = self.connection.get(query=query)

        return data

    def get_media_tracking(self, **kwargs):
        """
        Get media tracking
        :param progress: progress of entity. This is optional
        """
        self.connection.url = '{}/tracking'.format(self.connection.url)
        params = dict(appId=uiza.app_id)
        if kwargs:
            params.update(kwargs)
        query = self.url_encode(params=params)
        data = self.connection.get(query=query)

        return data

    def get_media_upload_detail(self, id):
        """
        Get media upload detail
        :param id: identifier of entity
        """
        self.connection.url = '{}/tracking'.format(self.connection.url)
        query = self.url_encode(params={'id': id, 'appId': uiza.app_id})
        data = self.connection.get(query=query)

        return data

    def get_aws_upload_key(self):
        """
        Return the bucket temporary upload storage & key for upload
        :param appId: appId
        """
        aws_sub_url = 'admin/app/config/aws'
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.entity.type,
            api_version=settings.uiza_api.entity.version,
            api_sub_url=aws_sub_url
        )
        query = self.url_encode(params={'appId': uiza.app_id})
        data = self.connection.get(query=query)

        return data
