API_CONCEPT = 'https://{workspace_api_domain}/{api_type}/{api_version}/{api_sub_url}'


def set_url(workspace_api_domain, api_type, api_version, api_sub_url):
    """

    :param workspace_api_domain:
    :param api_type:
    :param api_version:
    :param api_sub_url:
    :return:
    """
    return API_CONCEPT.format(
            workspace_api_domain=workspace_api_domain,
            api_type=api_type,
            api_version=api_version,
            api_sub_url=api_sub_url
        )
