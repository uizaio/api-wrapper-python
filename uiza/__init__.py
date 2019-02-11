from uiza.base.connections import Connection
from uiza.user.user import User
#
#
# class Client(Connection):
#
#     def __init__(self, workspace_api_domain: str, api_key: str, api_type: str, api_version: str, api_sub_url: str,
#                  **kwargs):
#         super().__init__(api_type, api_version, api_sub_url, workspace_api_domain, api_key, **kwargs)
#         self.user = User(workspace_api_domain, api_key)
#         self.workspace_api_domain = workspace_api_domain
#         self.api_key = api_key
#
