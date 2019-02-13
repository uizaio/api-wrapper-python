
class EntitiesErrors(object):
    ERR_UIZA_ENTITY_CREATE_NAME = 'name must be present'
    ERR_UIZA_ENTITY_CREATE_URL = 'url must be present'
    ERR_UIZA_ENTITY_CREATE_INPUT_TYPE = 'inputType must be present and must be in [http, s3, ftp, s3-uiza]'
    ERR_UIZA_ENTITY_RETRIEVE_ID = 'id must be present'
    ERR_UIZA_ENTITY_LIST_PUBLIST_TO_CDN = 'publishToCdn must be in [queue, not-ready, success, failed]'
    ERR_UIZA_ENTITY_UPDATE_ID = 'id must be present'
    ERR_UIZA_ENTITY_DELETE_ID = 'id must be present'
    ERR_UIZA_ENTITY_SEARCH_KEYWORD = 'keyword must be present'
    ERR_UIZA_ENTITY_PUBLISH_ID = 'id must be present'
    ERR_UIZA_ENTITY_GET_STATUS_PUBLISH_ID = 'id must be present'