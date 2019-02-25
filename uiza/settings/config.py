API_CONFIG = {
    "uiza_api": {
        "user": {
            "type": "api/public",
            "version": "v3",
            "sub_url": "admin/user"
        },
        "entity": {
            "type": "api/public",
            "version": "v3",
            "sub_url": "media/entity"
        },
        "category": {
            "type": "api/public",
            "version": "v3",
            "sub_url": "media/metadata"
        },
        "storage": {
            "type": "api/public",
            "version": "v3",
            "sub_url": "media/storage"
        },
        "livestreaming": {
            "type": "api/public",
            "version": "v3",
            "sub_url": "live/entity"
        },
        "callback": {
            "type": "api/public",
            "version": "v3",
            "sub_url": "media/entity/callback"
        },
        "analytic": {
            "type": "api/public",
            "version": "v3",
            "sub_url": "analytic/entity/video-quality"
        }
    }
}


class Settings(object):
    dict = None  # type: dict

    def __init__(self, d):
        self.dict = d
        for a, b in d.items():
            setattr(self, a, Settings(b) if isinstance(b, dict) else b)


settings = Settings(API_CONFIG)
